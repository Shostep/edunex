# payments - views.py
from django.shortcuts import render

def payment_callback(request):
    return render(request, 'payments/callback.html')

def verify_payment(request, reference):
    return render(request, 'payments/verify.html')
