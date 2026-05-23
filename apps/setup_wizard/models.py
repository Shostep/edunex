from django.db import models
from django.conf import settings

class SetupProgress(models.Model):
    """Track setup wizard progress"""
    step = models.PositiveIntegerField(default=1)
    completed_steps = models.JSONField(default=list)
    config_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'setup_progress'
