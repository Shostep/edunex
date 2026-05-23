# setup_wizard - views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.core.models import UniversityConfig

def redirect_to_setup(request):
    config = UniversityConfig.get()
    if config.is_setup_complete:
        return redirect('admission:home')
    return redirect('setup:wizard')

def setup_wizard(request, step=1):
    config = UniversityConfig.get()
    if config.is_setup_complete:
        return redirect('admission:home')
    return render(request, f'setup/step_{step}.html', {
        'step': step,
        'progress': int((step / 7) * 100),
    })

def setup_complete(request):
    return render(request, 'setup/complete.html')
