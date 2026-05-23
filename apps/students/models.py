from django.db import models
from django.conf import settings

class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('withdrawn', 'Withdrawn'),
        ('graduated', 'Graduated'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=20, unique=True)

    programme = models.ForeignKey('academics.Programme', on_delete=models.CASCADE)
    department = models.ForeignKey('academics.Department', on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=100)
    current_semester = models.ForeignKey('academics.Semester', on_delete=models.SET_NULL, null=True)

    application = models.OneToOneField('admission.Application', on_delete=models.CASCADE)
    admission_session = models.ForeignKey('academics.Session', on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    total_credits_earned = models.PositiveIntegerField(default=0)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    # Student services
    hostel_allocated = models.BooleanField(default=False)
    medical_cleared = models.BooleanField(default=False)
    library_cleared = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'students_student'

    def __str__(self):
        return f"{self.matric_number} - {self.user.full_name}"


class CourseRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)
    semester = models.ForeignKey('academics.Semester', on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        limit_choices_to={'role__in': ['hod', 'lecturer']}
    )
    is_approved = models.BooleanField(default=False)

    class Meta:
        db_table = 'students_course_registration'
        unique_together = ['student', 'course', 'semester']


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('excused', 'Excused'),
    ]

    course_registration = models.ForeignKey(CourseRegistration, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    marked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    marked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'students_attendance'
        unique_together = ['course_registration', 'date']


class StudentResult(models.Model):
    GRADE_CHOICES = [
        ('A', 'A - 5.0'), ('B', 'B - 4.0'), ('C', 'C - 3.0'),
        ('D', 'D - 2.0'), ('E', 'E - 1.0'), ('F', 'F - 0.0'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)
    semester = models.ForeignKey('academics.Semester', on_delete=models.CASCADE)

    ca_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    exam_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    grade_point = models.DecimalField(max_digits=3, decimal_places=2)
    is_released = models.BooleanField(default=False)

    class Meta:
        db_table = 'students_result'
        unique_together = ['student', 'course', 'semester']

    def save(self, *args, **kwargs):
        self.total_score = self.ca_score + self.exam_score
        if self.total_score >= 70: self.grade, self.grade_point = 'A', 5.0
        elif self.total_score >= 60: self.grade, self.grade_point = 'B', 4.0
        elif self.total_score >= 50: self.grade, self.grade_point = 'C', 3.0
        elif self.total_score >= 45: self.grade, self.grade_point = 'D', 2.0
        elif self.total_score >= 40: self.grade, self.grade_point = 'E', 1.0
        else: self.grade, self.grade_point = 'F', 0.0
        super().save(*args, **kwargs)


class TranscriptRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('ready', 'Ready'),
        ('delivered', 'Delivered'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=200)
    recipient_address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    fee_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    requested_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'students_transcript_request'
