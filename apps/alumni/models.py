from django.db import models
from django.conf import settings

class AlumniProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student = models.OneToOneField('students.Student', on_delete=models.CASCADE)

    graduation_year = models.PositiveIntegerField()
    final_cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    degree_class = models.CharField(max_length=50)  # First Class, Second Class Upper, etc.

    current_employer = models.CharField(max_length=200, blank=True)
    current_role = models.CharField(max_length=200, blank=True)
    contact_address = models.TextField(blank=True)

    is_profile_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'alumni_profile'


class CertificateVerification(models.Model):
    certificate_id = models.CharField(max_length=50, unique=True)
    alumni = models.ForeignKey(AlumniProfile, on_delete=models.CASCADE)
    programme = models.ForeignKey('academics.Programme', on_delete=models.CASCADE)
    session = models.ForeignKey('academics.Session', on_delete=models.CASCADE)

    is_valid = models.BooleanField(default=True)
    verified_count = models.PositiveIntegerField(default=0)
    last_verified_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'alumni_certificate_verification'
