from django.contrib import admin
from .models import IndigeneVerification

@admin.register(IndigeneVerification)
class IndigeneVerificationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'lga_of_origin', 'status', 'is_valid', 'verified_by', 'created_at']
    list_filter = ['status', 'state_of_origin', 'created_at']
    search_fields = ['applicant__email', 'applicant__surname', 'lga_of_origin']
    actions = ['verify_selected', 'reject_selected']

    def verify_selected(self, request, queryset):
        from django.utils import timezone
        queryset.update(status='verified', verified_by=request.user, verified_at=timezone.now())
    verify_selected.short_description = "Mark selected as verified"

    def reject_selected(self, request, queryset):
        queryset.update(status='rejected')
    reject_selected.short_description = "Mark selected as rejected"
