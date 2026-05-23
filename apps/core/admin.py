from django.contrib import admin
from .models import UniversityConfig, ActivityLog, Notification

@admin.register(UniversityConfig)
class UniversityConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'state', 'is_setup_complete', 'created_at']
    readonly_fields = ['created_at']

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'ip_address', 'timestamp']
    list_filter = ['action', 'timestamp']
    search_fields = ['user__email', 'description']
    date_hierarchy = 'timestamp'

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'priority', 'is_read', 'created_at']
    list_filter = ['priority', 'is_read', 'created_at']
