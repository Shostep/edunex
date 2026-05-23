# lecturers - views.py
from django.shortcuts import render

def lecturer_dashboard(request):
    return render(request, 'lecturers/dashboard.html')

def my_courses(request):
    return render(request, 'lecturers/courses.html')

def mark_attendance(request, course_id):
    return render(request, 'lecturers/attendance.html')

def enter_ca_scores(request, course_id):
    return render(request, 'lecturers/ca.html')

def enter_exam_scores(request, course_id):
    return render(request, 'lecturers/exam.html')

def class_performance(request, course_id):
    return render(request, 'lecturers/performance.html')

def submit_results(request, course_id):
    return render(request, 'lecturers/submit_results.html')
