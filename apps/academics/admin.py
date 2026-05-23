from django.contrib import admin
from .models import Faculty, Department, Programme, Course, Session, Semester

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'faculty', 'hod']
    list_filter = ['faculty']
    search_fields = ['name', 'code']

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'department', 'degree_type', 'duration_years', 'is_active']
    list_filter = ['degree_type', 'is_active', 'department']
    search_fields = ['name', 'code']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'units', 'level', 'semester', 'is_elective']
    list_filter = ['level', 'semester', 'is_elective', 'department']
    search_fields = ['code', 'title']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current']

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['session', 'name', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'name']
