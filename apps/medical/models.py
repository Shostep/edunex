from django.db import models
from django.conf import settings

class MedicalRecord(models.Model):
    student = models.OneToOneField('students.Student', on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5, blank=True)
    genotype = models.CharField(max_length=5, blank=True)
    allergies = models.TextField(blank=True)
    chronic_conditions = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=200, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True)

    class Meta:
        db_table = 'medical_record'


class MedicalAppointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    diagnosis = models.TextField(blank=True)
    treatment = models.TextField(blank=True)
    attended_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        limit_choices_to={'role': 'medical_officer'}
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'medical_appointment'
