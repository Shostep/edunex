from django.contrib import admin
from .models import MedicalRecord, MedicalAppointment

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['student', 'blood_group', 'genotype']
    search_fields = ['student__matric_number']

@admin.register(MedicalAppointment)
class MedicalAppointmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'appointment_date', 'status', 'attended_by']
    list_filter = ['status', 'appointment_date']
