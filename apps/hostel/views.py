# hostel - views.py
from django.shortcuts import render

def hostel_dashboard(request):
    return render(request, 'hostel/dashboard.html')

def room_management(request):
    return render(request, 'hostel/rooms.html')

def allocate_student(request):
    return render(request, 'hostel/allocate.html')

def view_allocations(request):
    return render(request, 'hostel/allocations.html')
