from django.contrib import admin
from django.utils.html import format_html
from .models import AdmissionSession, SubjectRequirement, Application, ScreeningActivity, AdmissionList, AdmissionListEntry

@admin.register(AdmissionSession)
class AdmissionSessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'session_type', 'is_application_open', 'is_screening_active', 'is_active']
    list_filter = ['session_type', 'is_active']
    date_hierarchy = 'application_opens'

@admin.register(SubjectRequirement)
class SubjectRequirementAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'importance', 'department', 'programme', 'weight', 'is_active']
    list_filter = ['importance', 'department', 'is_active']
    search_fields = ['subject_name']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['application_number', 'applicant_name', 'first_choice', 'status_badge', 'screening_score', 'created_at']
    list_filter = ['status', 'admission_session', 'first_choice']
    search_fields = ['application_number', 'applicant__email', 'jamb_reg_number']
    date_hierarchy = 'created_at'
    actions = ['bulk_admit', 'run_auto_screening']

    def applicant_name(self, obj):
        return obj.applicant.full_name

    def status_badge(self, obj):
        colors = {
            'draft': 'gray', 'submitted': 'blue', 'paid': 'green',
            'documents_uploaded': 'yellow', 'under_screening': 'orange',
            'screening_passed': 'green', 'screening_flagged': 'red',
            'admitted': 'purple', 'not_admitted': 'red',
            'accepted': 'green', 'declined': 'gray'
        }
        color = colors.get(obj.status, 'gray')
        return format_html(
            '<span style="background:{};color:white;padding:2px 8px;border-radius:12px;font-size:12px;">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'Status'

    def bulk_admit(self, request, queryset):
        admitted = 0
        for app in queryset.filter(status='screening_passed'):
            app.status = 'admitted'
            app.admitted_programme = app.first_choice
            app.save()
            app.generate_matric_number()
            admitted += 1
        self.message_user(request, f"Admitted {admitted} applicants")
    bulk_admit.short_description = "Admit selected (auto-screened)"

    def run_auto_screening(self, request, queryset):
        for app in queryset.filter(status='documents_uploaded'):
            app.run_auto_screening()
    run_auto_screening.short_description = "Run auto-screening on selected"

@admin.register(ScreeningActivity)
class ScreeningActivityAdmin(admin.ModelAdmin):
    list_display = ['application', 'action', 'performed_by', 'created_at']
    list_filter = ['action', 'created_at']

@admin.register(AdmissionList)
class AdmissionListAdmin(admin.ModelAdmin):
    list_display = ['programme', 'list_type', 'is_published', 'published_at']
    list_filter = ['is_published', 'list_type']

@admin.register(AdmissionListEntry)
class AdmissionListEntryAdmin(admin.ModelAdmin):
    list_display = ['admission_list', 'application', 'position', 'screening_score']
    list_filter = ['admission_list']
    ordering = ['position']
