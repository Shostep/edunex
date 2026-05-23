# alumni - views.py
from django.shortcuts import render

def alumni_dashboard(request):
    return render(request, 'alumni/dashboard.html')

def alumni_transcript(request):
    return render(request, 'alumni/transcript.html')

def certificate_verification(request):
    return render(request, 'alumni/certificate.html')

def public_verify_certificate(request, cert_id):
    return render(request, 'alumni/public_verify.html')
