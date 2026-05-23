from django.contrib import admin
from .models import LecturerCourseAssignment, ResultSubmission

@admin.register(LecturerCourseAssignment)
class LecturerCourseAssignmentAdmin(admin.ModelAdmin):
    list_display = ['lecturer', 'course', 'semester', 'is_active']
    list_filter = ['is_active', 'semester']

@admin.register(ResultSubmission)
class ResultSubmissionAdmin(admin.ModelAdmin):
    list_display = ['lecturer', 'course', 'semester', 'status', 'submitted_at']
    list_filter = ['status', 'semester']
