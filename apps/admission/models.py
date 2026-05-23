from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

class AdmissionSession(models.Model):
    SESSION_TYPES = [
        ('utme', 'UTME'),
        ('direct_entry', 'Direct Entry'),
        ('transfer', 'Transfer'),
        ('pg', 'Postgraduate'),
    ]

    name = models.CharField(max_length=50)
    session_type = models.CharField(max_length=20, choices=SESSION_TYPES)

    # Dates
    application_opens = models.DateTimeField()
    application_closes = models.DateTimeField()
    screening_starts = models.DateTimeField()
    screening_ends = models.DateTimeField()
    admission_list_published = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=False)

    # Requirements (overridden by department config)
    min_jamb_score = models.PositiveIntegerField(default=180)
    min_olevel_credits = models.PositiveIntegerField(default=5)
    max_age = models.PositiveIntegerField(null=True, blank=True)

    # Fees (overridden by university config)
    screening_fee = models.DecimalField(max_digits=10, decimal_places=2, default=2000)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=3000)
    acceptance_fee = models.DecimalField(max_digits=10, decimal_places=2, default=25000)
    medical_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5000)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'admission_session'
        ordering = ['-application_opens']

    def __str__(self):
        return f"{self.name} ({self.get_session_type_display()})"

    @property
    def is_application_open(self):
        now = timezone.now()
        return self.is_active and self.application_opens <= now <= self.application_closes

    @property
    def is_screening_active(self):
        now = timezone.now()
        return self.is_active and self.screening_starts <= now <= self.screening_ends

    @property
    def total_screening_fee(self):
        return self.screening_fee + self.service_charge


class SubjectRequirement(models.Model):
    """HOD-configurable subject requirements per department/programme"""

    IMPORTANCE_CHOICES = [
        ('compulsory', 'Compulsory - Must be present'),
        ('required', 'Required - Must be present'),
        ('acceptable', 'Acceptable - Counts if present'),
    ]

    department = models.ForeignKey('academics.Department', on_delete=models.CASCADE, related_name='subject_requirements')
    programme = models.ForeignKey('academics.Programme', on_delete=models.CASCADE, null=True, blank=True, related_name='subject_requirements')
    subject_name = models.CharField(max_length=100)
    importance = models.CharField(max_length=15, choices=IMPORTANCE_CHOICES, default='required')
    weight = models.DecimalField(max_digits=4, decimal_places=2, default=1.0)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'hod'})
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'admission_subject_requirement'
        unique_together = [['department', 'programme', 'subject_name']]
        ordering = ['-importance', 'subject_name']

    def __str__(self):
        scope = f"({self.programme.code})" if self.programme else "(Dept)"
        return f"{self.subject_name} - {self.get_importance_display()} {scope}"


class Application(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('payment_pending', 'Payment Pending'),
        ('paid', 'Payment Confirmed'),
        ('documents_uploaded', 'Documents Uploaded'),
        ('under_screening', 'Under E-Screening'),
        ('screening_passed', 'E-Screening Passed'),
        ('screening_flagged', 'Flagged for Review'),
        ('admitted', 'Admitted'),
        ('not_admitted', 'Not Admitted'),
        ('accepted', 'Offer Accepted'),
        ('declined', 'Offer Declined'),
    ]

    # Core IDs
    application_number = models.CharField(max_length=30, unique=True)
    admission_session = models.ForeignKey(AdmissionSession, on_delete=models.CASCADE)

    # Applicant
    applicant = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Programme Choices
    first_choice = models.ForeignKey('academics.Programme', on_delete=models.CASCADE, related_name='first_choice_apps')
    second_choice = models.ForeignKey('academics.Programme', on_delete=models.CASCADE, related_name='second_choice_apps', null=True, blank=True)

    # Indigene link
    indigene_verification = models.ForeignKey('indigene.IndigeneVerification', on_delete=models.SET_NULL, null=True, blank=True)
    is_indigene = models.BooleanField(default=False)

    # Personal Info
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male','Male'),('female','Female')])
    marital_status = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50, default='Nigerian')
    state_of_origin = models.CharField(max_length=50)
    local_govt = models.CharField(max_length=100)
    home_address = models.TextField()
    phone = models.CharField(max_length=15)
    alt_phone = models.CharField(max_length=15, blank=True)

    # Next of Kin
    next_of_kin_name = models.CharField(max_length=200)
    next_of_kin_phone = models.CharField(max_length=15)
    next_of_kin_relationship = models.CharField(max_length=50)
    next_of_kin_address = models.TextField()

    # Academic Info
    jamb_reg_number = models.CharField(max_length=20, blank=True)
    jamb_score = models.PositiveIntegerField(null=True, blank=True)
    jamb_subjects = models.JSONField(default=list, blank=True)

    # O'Level (structured JSON)
    olevel_results = models.JSONField(default=list, blank=True)

    # Previous qualification (for DE/Transfer/PG)
    previous_institution = models.CharField(max_length=200, blank=True)
    previous_qualification = models.CharField(max_length=100, blank=True)
    previous_grade = models.CharField(max_length=20, blank=True)

    # Documents
    passport_photo = models.ImageField(upload_to='admission/%Y/passports/')
    olevel_result_1 = models.FileField(upload_to='admission/%Y/olevel/')
    olevel_result_2 = models.FileField(upload_to='admission/%Y/olevel/', blank=True)
    birth_certificate = models.FileField(upload_to='admission/%Y/birth/')
    jamb_result = models.FileField(upload_to='admission/%Y/jamb/', blank=True)
    local_govt_cert = models.FileField(upload_to='admission/%Y/lga/', blank=True)

    # Document verification
    passport_verified = models.BooleanField(default=False)
    olevel_verified = models.BooleanField(default=False)
    birth_cert_verified = models.BooleanField(default=False)
    jamb_result_verified = models.BooleanField(default=False)
    lga_cert_verified = models.BooleanField(default=False)

    # O'Level API verification
    olevel_api_verified = models.BooleanField(default=False)
    olevel_api_mismatch = models.BooleanField(default=False)
    olevel_api_response = models.JSONField(default=dict, blank=True)

    # Payment
    screening_fee_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    service_charge_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_reference = models.CharField(max_length=100, blank=True)
    payment_gateway_ref = models.CharField(max_length=100, blank=True)
    payment_status = models.CharField(max_length=20, default='pending')
    paid_at = models.DateTimeField(null=True, blank=True)

    # E-Screening
    screening_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    screening_remarks = models.TextField(blank=True)
    auto_screening_results = models.JSONField(default=dict, blank=True)

    screened_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='screened_apps',
        limit_choices_to={'role__in': ['admin', 'registrar']}
    )
    screened_at = models.DateTimeField(null=True, blank=True)

    # Admission
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='draft')
    admitted_programme = models.ForeignKey('academics.Programme', on_delete=models.SET_NULL, null=True, blank=True)
    admission_list_number = models.PositiveIntegerField(null=True, blank=True)
    matric_number = models.CharField(max_length=20, blank=True)

    # Acceptance
    acceptance_fee_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    medical_fee_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    acceptance_paid_at = models.DateTimeField(null=True, blank=True)
    offer_responded_at = models.DateTimeField(null=True, blank=True)

    # Meta
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    submitted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'admission_application'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['application_number']),
            models.Index(fields=['status']),
            models.Index(fields=['jamb_reg_number']),
            models.Index(fields=['admission_session', 'status']),
        ]

    def save(self, *args, **kwargs):
        if not self.application_number:
            year = timezone.now().year
            self.application_number = f"EDU/{year}/{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)

    @property
    def is_payment_complete(self):
        return self.payment_status == 'success' and self.total_paid >= self.admission_session.total_screening_fee

    @property
    def are_documents_complete(self):
        required = [self.passport_photo, self.olevel_result_1, self.birth_certificate]
        return all(required)

    @property
    def are_documents_verified(self):
        return self.passport_verified and self.olevel_verified and self.birth_cert_verified

    @property
    def age(self):
        if self.date_of_birth:
            today = timezone.now().date()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None

    @property
    def olevel_credit_count(self):
        credit_grades = ['A1', 'B2', 'B3', 'C4', 'C5', 'C6']
        count = 0
        for sitting in self.olevel_results:
            for subject in sitting.get('subjects', []):
                if subject.get('grade') in credit_grades:
                    count += 1
        return count

    def generate_matric_number(self):
        if self.matric_number:
            return self.matric_number

        dept_code = self.admitted_programme.department.code
        year = timezone.now().year
        count = Application.objects.filter(
            admitted_programme=self.admitted_programme,
            status__in=['admitted', 'accepted'],
            created_at__year=year
        ).count() + 1

        self.matric_number = f"{dept_code}/{year}/{count:04d}"
        self.save()
        return self.matric_number


class ScreeningActivity(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='screening_activities')
    action = models.CharField(max_length=50)
    description = models.TextField()
    performed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    old_status = models.CharField(max_length=25, blank=True)
    new_status = models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'admission_screening_activity'
        ordering = ['-created_at']


class AdmissionList(models.Model):
    admission_session = models.ForeignKey(AdmissionSession, on_delete=models.CASCADE)
    programme = models.ForeignKey('academics.Programme', on_delete=models.CASCADE)
    list_type = models.CharField(max_length=20, choices=[
        ('merit', 'Merit List'),
        ('supplementary', 'Supplementary'),
        ('second_choice', 'Second Choice'),
    ])
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'admission_list'

    def __str__(self):
        return f"{self.programme.name} - {self.get_list_type_display()}"


class AdmissionListEntry(models.Model):
    admission_list = models.ForeignKey(AdmissionList, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    screening_score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'admission_list_entry'
        ordering = ['position']
        unique_together = ['admission_list', 'application']
