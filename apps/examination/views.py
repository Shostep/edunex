# examination - views.py
from django.shortcuts import render

def exam_timetable(request):
    return render(request, 'examination/timetable.html')

def exam_clearance(request):
    return render(request, 'examination/clearance.html')
