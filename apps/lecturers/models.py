from django.db import models
from django.conf import settings

class LecturerCourseAssignment(models.Model):
    lecturer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'lecturer'},
        related_name='assigned_courses'
    )
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)
    semester = models.ForeignKey('academics.Semester', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'lecturers_course_assignment'
        unique_together = ['lecturer', 'course', 'semester']


class ResultSubmission(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved by HOD'),
        ('rejected', 'Rejected'),
    ]

    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)
    semester = models.ForeignKey('academics.Semester', on_delete=models.CASCADE)

    total_students = models.PositiveIntegerField(default=0)
    submitted_count = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    submitted_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='approved_results',
        limit_choices_to={'role': 'hod'}
    )
    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'lecturers_result_submission'
