from django.db import models
from django.conf import settings

class Faculty(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'academics_faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    hod = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        limit_choices_to={'role': 'hod'},
        related_name='department_head'
    )

    class Meta:
        db_table = 'academics_department'

    def __str__(self):
        return f"{self.name} ({self.code})"

class Programme(models.Model):
    DEGREE_CHOICES = [
        ('bsc', 'Bachelor of Science'),
        ('bed', 'Bachelor of Education'),
        ('nce', 'Nigeria Certificate in Education'),
        ('pgde', 'Postgraduate Diploma in Education'),
        ('msc', 'Master of Science'),
        ('phd', 'Doctor of Philosophy'),
    ]

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    degree_type = models.CharField(max_length=10, choices=DEGREE_CHOICES)
    duration_years = models.PositiveIntegerField(default=4)
    required_credits = models.PositiveIntegerField(default=120)
    is_active = models.BooleanField(default=True)

    # Screening overrides
    min_jamb_score = models.PositiveIntegerField(null=True, blank=True)
    min_olevel_credits = models.PositiveIntegerField(null=True, blank=True)
    required_jamb_subjects = models.JSONField(default=list, blank=True)

    class Meta:
        db_table = 'academics_programme'

    def __str__(self):
        return f"{self.name} ({self.code})"

class Course(models.Model):
    SEMESTER_CHOICES = [
        ('first', 'First Semester'),
        ('second', 'Second Semester'),
    ]

    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    units = models.PositiveIntegerField(default=3)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(choices=[(100,100),(200,200),(300,300),(400,400),(500,500)])
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    is_elective = models.BooleanField(default=False)
    max_students = models.PositiveIntegerField(default=200)
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)

    class Meta:
        db_table = 'academics_course'

    def __str__(self):
        return f"{self.code} - {self.title}"

class Session(models.Model):
    name = models.CharField(max_length=20, help_text="e.g., 2025/2026")
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)

    class Meta:
        db_table = 'academics_session'
        ordering = ['-start_date']

    def save(self, *args, **kwargs):
        if self.is_current:
            Session.objects.filter(is_current=True).update(is_current=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Semester(models.Model):
    SEMESTER_CHOICES = [
        ('first', 'First Semester'),
        ('second', 'Second Semester'),
    ]

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)

    class Meta:
        db_table = 'academics_semester'
        unique_together = ['session', 'name']

    def __str__(self):
        return f"{self.session.name} - {self.name}"
