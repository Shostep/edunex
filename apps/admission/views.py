# admission - views.py
from django.shortcuts import render

# Public
def admission_home(request):
    return render(request, 'admission/home.html')

def public_admission_list(request):
    return render(request, 'admission/list.html')

def verify_admission(request):
    return render(request, 'admission/verify.html')

# Application flow
def start_application(request, session_id):
    return render(request, 'admission/start.html')

def step_personal(request, app_id):
    return render(request, 'admission/personal.html')

def step_academic(request, app_id):
    return render(request, 'admission/academic.html')

def step_payment(request, app_id):
    return render(request, 'admission/payment.html')

def payment_callback(request):
    return render(request, 'admission/payment_callback.html')

def step_upload(request, app_id):
    return render(request, 'admission/upload.html')

def application_tracker(request, app_id):
    return render(request, 'admission/tracker.html')

# Admission response
def respond_to_admission(request, app_id):
    return render(request, 'admission/respond.html')

def pay_acceptance_fee(request, app_id):
    return render(request, 'admission/acceptance.html')

def acceptance_callback(request):
    return render(request, 'admission/acceptance_callback.html')

# Admin
def admin_screening_dashboard(request):
    return render(request, 'admission/admin_screening.html')

def admin_verify_document(request, app_id, doc_type):
    return render(request, 'admission/admin_verify.html')

def admin_manual_screen(request, app_id):
    return render(request, 'admission/admin_screen.html')

def publish_admission_list(request):
    return render(request, 'admission/publish.html')
