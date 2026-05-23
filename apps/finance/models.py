from django.db import models
from django.conf import settings

class FeeItem(models.Model):
    FEE_TYPES = [
        ('tuition', 'Tuition Fee'),
        ('acceptance', 'Acceptance Fee'),
        ('departmental', 'Departmental Fee'),
        ('library', 'Library Fee'),
        ('hostel', 'Hostel Fee'),
        ('exam', 'Examination Fee'),
        ('medical', 'Medical Fee'),
        ('sports', 'Sports Fee'),
        ('transcript', 'Transcript Fee'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    fee_type = models.CharField(max_length=20, choices=FEE_TYPES)
    programme = models.ForeignKey('academics.Programme', on_delete=models.CASCADE)
    level = models.PositiveIntegerField(choices=[(100,100),(200,200),(300,300),(400,400),(500,500)])
    session = models.ForeignKey('academics.Session', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_mandatory = models.BooleanField(default=True)
    due_date = models.DateField()

    class Meta:
        db_table = 'finance_fee_item'
        unique_together = ['name', 'programme', 'level', 'session']


class Payment(models.Model):
    METHOD_CHOICES = [
        ('card', 'Debit Card'),
        ('transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
        ('bank', 'Bank Deposit'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]

    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, null=True, blank=True)
    applicant = models.ForeignKey('admission.Application', on_delete=models.CASCADE, null=True, blank=True)
    fee_item = models.ForeignKey(FeeItem, on_delete=models.CASCADE, null=True, blank=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    transaction_reference = models.CharField(max_length=100, unique=True)
    payment_gateway_ref = models.CharField(max_length=100, blank=True)
    receipt_number = models.CharField(max_length=50, unique=True)

    paid_at = models.DateTimeField(null=True, blank=True)
    recorded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'finance_payment'


class StudentBalance(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    session = models.ForeignKey('academics.Session', on_delete=models.CASCADE)
    total_billed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'finance_student_balance'
        unique_together = ['student', 'session']

    @property
    def balance(self):
        return self.total_billed - self.total_paid

    @property
    def is_fully_paid(self):
        return self.balance <= 0
