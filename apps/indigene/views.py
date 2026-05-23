# indigene - views.py
from django.shortcuts import render

def indigene_home(request):
    return render(request, 'indigene/home.html')
