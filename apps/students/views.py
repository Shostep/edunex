# students - views.py
from django.shortcuts import render

def student_dashboard(request):
    return render(request, 'students/dashboard.html')

def course_registration(request):
    return render(request, 'students/courses.html')

def view_results(request):
    return render(request, 'students/results.html')

def view_fees(request):
    return render(request, 'students/fees.html')

def request_transcript(request):
    return render(request, 'students/transcript.html')

def view_timetable(request):
    return render(request, 'students/timetable.html')

def hostel_application(request):
    return render(request, 'students/hostel.html')

def medical_dashboard(request):
    return render(request, 'students/medical.html')

def library_dashboard(request):
    return render(request, 'students/library.html')

def id_card(request):
    return render(request, 'students/id_card.html')

def student_profile(request):
    return render(request, 'students/profile.html')
