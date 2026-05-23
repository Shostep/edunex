# academics - views.py
from django.shortcuts import render

def faculty_list(request):
    return render(request, 'academics/faculties.html')

def department_list(request):
    return render(request, 'academics/departments.html')

def programme_list(request):
    return render(request, 'academics/programmes.html')

def course_list(request):
    return render(request, 'academics/courses.html')
