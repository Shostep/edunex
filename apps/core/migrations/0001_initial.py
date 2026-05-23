from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=20, unique=True)),
                ('state', models.CharField(max_length=50)),
                ('logo_url', models.URLField(blank=True)),
                ('primary_color', models.CharField(default='#1e40af', max_length=7)),
                ('secondary_color', models.CharField(default='#3b82f6', max_length=7)),
                ('indigene_verification_required', models.BooleanField(default=True)),
                ('indigene_lgas', models.JSONField(blank=True, default=list)),
                ('indigene_verification_fee', models.DecimalField(decimal_places=2, default=5000, max_digits=10)),
                ('screening_fee_indigene', models.DecimalField(decimal_places=2, default=2000, max_digits=10)),
                ('screening_fee_non_indigene', models.DecimalField(decimal_places=2, default=5000, max_digits=10)),
                ('service_charge', models.DecimalField(decimal_places=2, default=3000, max_digits=10)),
                ('acceptance_fee', models.DecimalField(decimal_places=2, default=25000, max_digits=10)),
                ('medical_fee', models.DecimalField(decimal_places=2, default=5000, max_digits=10)),
                ('min_jamb_score', models.PositiveIntegerField(default=180)),
                ('min_olevel_credits', models.PositiveIntegerField(default=5)),
                ('indigene_bonus_points', models.DecimalField(decimal_places=2, default=10, max_digits=4)),
                ('deadline_policy', models.JSONField(blank=True, default=dict)),
                ('is_setup_complete', models.BooleanField(default=False)),
                ('setup_completed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'core_university_config',
            },
        ),
        migrations.AddConstraint(
            model_name='universityconfig',
            constraint=models.UniqueConstraint(fields=('id',), name='single_config'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('priority', models.CharField(choices=[('low', 'Low'), ('normal', 'Normal'), ('urgent', 'Urgent'), ('critical', 'Critical')], default='normal', max_length=10)),
                ('category', models.CharField(max_length=30)),
                ('action_url', models.URLField(blank=True)),
                ('action_text', models.CharField(blank=True, max_length=50)),
                ('is_read', models.BooleanField(default=False)),
                ('read_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_notification',
                'ordering': ['-priority', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_activity_log',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AddIndex(
            model_name='activitylog',
            index=models.Index(fields=['user', '-timestamp'], name='core_activi_user_id_7c0f9f_idx'),
        ),
    ]
