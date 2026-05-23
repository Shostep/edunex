# accounts - views.py
from django.shortcuts import render

def custom_login(request):
    return render(request, 'accounts/login.html')
