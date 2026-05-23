from django.db import models

class PaystackTransaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('abandoned', 'Abandoned'),
    ]

    reference = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    amount_kobo = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    paystack_reference = models.CharField(max_length=100, blank=True)
    paystack_authorization_url = models.URLField(blank=True)

    metadata = models.JSONField(default=dict, blank=True)
    response_data = models.JSONField(default=dict, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'payments_paystack_transaction'
