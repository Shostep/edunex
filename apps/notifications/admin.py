from django.contrib import admin
from .models import NotificationLog

@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'channel', 'status', 'sent_at']
    list_filter = ['channel', 'status', 'created_at']
