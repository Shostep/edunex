from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'System Admin'),
        ('registrar', 'Registrar'),
        ('bursar', 'Bursar'),
        ('hod', 'Head of Department'),
        ('lecturer', 'Lecturer'),
        ('student', 'Student'),
        ('applicant', 'Applicant'),
        ('medical_officer', 'Medical Officer'),
        ('librarian', 'Librarian'),
        ('hostel_admin', 'Hostel Admin'),
        ('alumni', 'Alumni'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='applicant')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'surname', 'first_name']

    class Meta:
        db_table = 'accounts_user'

    def __str__(self):
        return f"{self.email} ({self.role})"

    @property
    def full_name(self):
        return f"{self.surname} {self.first_name} {self.other_names}".strip()

    def migrate_to_student(self, matric_number):
        """Called when applicant is admitted."""
        self.role = 'student'
        self.username = matric_number
        self.save()
