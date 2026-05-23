from django.contrib import admin
from .models import FeeItem, Payment, StudentBalance

@admin.register(FeeItem)
class FeeItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'fee_type', 'programme', 'level', 'amount', 'is_mandatory']
    list_filter = ['fee_type', 'is_mandatory', 'programme']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['receipt_number', 'student', 'amount', 'method', 'status', 'created_at']
    list_filter = ['status', 'method', 'created_at']
    search_fields = ['receipt_number', 'student__matric_number']

@admin.register(StudentBalance)
class StudentBalanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'session', 'total_billed', 'total_paid', 'balance']
    list_filter = ['session']
