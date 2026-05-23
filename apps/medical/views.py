# medical - views.py
from django.shortcuts import render

def medical_dashboard(request):
    return render(request, 'medical/dashboard.html')

def student_records(request):
    return render(request, 'medical/records.html')

def appointments(request):
    return render(request, 'medical/appointments.html')
