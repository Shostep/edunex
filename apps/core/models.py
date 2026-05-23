from django.db import models
from django.conf import settings

class UniversityConfig(models.Model):
    """Single-row configuration per university instance"""

    # Identity
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20, unique=True)
    state = models.CharField(max_length=50)
    logo_url = models.URLField(blank=True)
    primary_color = models.CharField(max_length=7, default="#1e40af")
    secondary_color = models.CharField(max_length=7, default="#3b82f6")

    # Indigene
    indigene_verification_required = models.BooleanField(default=True)
    indigene_lgas = models.JSONField(default=list, blank=True)
    indigene_verification_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5000)

    # Fees
    screening_fee_indigene = models.DecimalField(max_digits=10, decimal_places=2, default=2000)
    screening_fee_non_indigene = models.DecimalField(max_digits=10, decimal_places=2, default=5000)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=3000)
    acceptance_fee = models.DecimalField(max_digits=10, decimal_places=2, default=25000)
    medical_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5000)

    # Screening defaults
    min_jamb_score = models.PositiveIntegerField(default=180)
    min_olevel_credits = models.PositiveIntegerField(default=5)
    indigene_bonus_points = models.DecimalField(max_digits=4, decimal_places=2, default=10)

    # Deadlines
    deadline_policy = models.JSONField(default=dict, blank=True)

    # Setup status
    is_setup_complete = models.BooleanField(default=False)
    setup_completed_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'core_university_config'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='single_config')
        ]

    @classmethod
    def get(cls):
        config, _ = cls.objects.get_or_create(id=1)
        return config

class ActivityLog(models.Model):
    """Audit everything"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    description = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'core_activity_log'
        ordering = ['-timestamp']
        indexes = [models.Index(fields=['user', '-timestamp'])]

class Notification(models.Model):
    PRIORITY_CHOICES = [('low', 'Low'), ('normal', 'Normal'), ('urgent', 'Urgent'), ('critical', 'Critical')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='normal')
    category = models.CharField(max_length=30)
    action_url = models.URLField(blank=True)
    action_text = models.CharField(max_length=50, blank=True)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'core_notification'
        ordering = ['-priority', '-created_at']
