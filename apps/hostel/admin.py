from django.contrib import admin
from .models import HostelBlock, HostelRoom, HostelAllocation

@admin.register(HostelBlock)
class HostelBlockAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'gender', 'total_rooms']

@admin.register(HostelRoom)
class HostelRoomAdmin(admin.ModelAdmin):
    list_display = ['block', 'room_number', 'capacity', 'occupied', 'is_available']
    list_filter = ['block', 'is_available']

@admin.register(HostelAllocation)
class HostelAllocationAdmin(admin.ModelAdmin):
    list_display = ['student', 'room', 'session', 'is_active']
    list_filter = ['is_active', 'session']
