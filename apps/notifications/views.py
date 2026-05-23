# notifications - views.py
from django.shortcuts import render

def notification_list(request):
    return render(request, 'notifications/list.html')

def mark_read(request, notif_id):
    return render(request, 'notifications/mark_read.html')

def mark_all_read(request):
    return render(request, 'notifications/mark_all_read.html')
