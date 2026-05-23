# indigene - views.py
from django.shortcuts import render

def indigene_home(request):
    return render(request, 'indigene/home.html')

def apply_indigene(request):
    return render(request, 'indigene/apply.html')

def upload_indigene_docs(request, app_id):
    return render(request, 'indigene/upload.html')

def pay_indigene_fee(request, app_id):
    return render(request, 'indigene/pay.html')

def indigene_status(request, app_id):
    return render(request, 'indigene/status.html')

def indigene_tracker(request, app_id):
    return render(request, 'indigene/tracker.html')
