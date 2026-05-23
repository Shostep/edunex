# finance - views.py
from django.shortcuts import render

def bursar_dashboard(request):
    return render(request, 'finance/dashboard.html')

def fee_structure(request):
    return render(request, 'finance/fee_structure.html')

def payment_records(request):
    return render(request, 'finance/payments.html')

def financial_reports(request):
    return render(request, 'finance/reports.html')

def receipts(request):
    return render(request, 'finance/receipts.html')

def outstanding_balances(request):
    return render(request, 'finance/balances.html')
