from django.contrib import admin
from .models import PaystackTransaction

@admin.register(PaystackTransaction)
class PaystackTransactionAdmin(admin.ModelAdmin):
    list_display = ['reference', 'email', 'amount_kobo', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['reference', 'email']
