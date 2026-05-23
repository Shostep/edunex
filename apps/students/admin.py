from django.contrib import admin
from .models import Student, CourseRegistration, Attendance, StudentResult, TranscriptRequest

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['matric_number', 'user_name', 'programme', 'level', 'status', 'cgpa']
    list_filter = ['status', 'level', 'programme']
    search_fields = ['matric_number', 'user__email', 'user__surname']

    def user_name(self, obj):
        return obj.user.full_name

@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'semester', 'is_approved']
    list_filter = ['is_approved', 'semester']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['course_registration', 'date', 'status', 'marked_by']
    list_filter = ['status', 'date']

@admin.register(StudentResult)
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'total_score', 'grade', 'is_released']
    list_filter = ['grade', 'is_released', 'semester']
    actions = ['release_results']

    def release_results(self, request, queryset):
        queryset.update(is_released=True)
    release_results.short_description = "Release selected results"

@admin.register(TranscriptRequest)
class TranscriptRequestAdmin(admin.ModelAdmin):
    list_display = ['student', 'purpose', 'status', 'requested_at']
    list_filter = ['status']
