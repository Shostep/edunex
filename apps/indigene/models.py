from django.db import models
from django.conf import settings
from django.utils import timezone

class IndigeneVerification(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
        ('expired', 'Expired'),
    ]

    applicant = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Documents
    indigene_certificate = models.FileField(upload_to='indigene/certs/%Y/')
    birth_certificate = models.FileField(upload_to='indigene/birth/%Y/')
    lga_identification = models.FileField(upload_to='indigene/lga/%Y/')
    affidavit = models.FileField(upload_to='indigene/affidavit/%Y/', blank=True)

    # Details
    lga_of_origin = models.CharField(max_length=100)
    state_of_origin = models.CharField(max_length=50)

    # Review
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    verified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='verified_indigenes',
        limit_choices_to={'role__in': ['admin', 'registrar']}
    )
    verified_at = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(blank=True)
    review_notes = models.TextField(blank=True)

    # Validity (4 years = one degree cycle)
    valid_until = models.DateField(null=True, blank=True)

    # Payment
    verification_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5000)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_reference = models.CharField(max_length=100, blank=True)
    payment_status = models.CharField(max_length=20, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'indigene_verification'

    def __str__(self):
        return f"{self.applicant.full_name} - {self.status}"

    @property
    def is_valid(self):
        if self.status != 'verified':
            return False
        if self.valid_until and self.valid_until < timezone.now().date():
            return False
        return True

    def save(self, *args, **kwargs):
        if not self.valid_until and self.verified_at:
            self.valid_until = self.verified_at.date() + timezone.timedelta(days=1461)  # 4 years
        super().save(*args, **kwargs)
