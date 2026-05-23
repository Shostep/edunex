from django.contrib import admin
from .models import AlumniProfile, CertificateVerification

@admin.register(AlumniProfile)
class AlumniProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'graduation_year', 'final_cgpa', 'degree_class']
    list_filter = ['graduation_year', 'degree_class']

@admin.register(CertificateVerification)
class CertificateVerificationAdmin(admin.ModelAdmin):
    list_display = ['certificate_id', 'alumni', 'is_valid', 'verified_count']
    list_filter = ['is_valid']
