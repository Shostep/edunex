from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from apps.core.models import UniversityConfig

def redirect_to_setup(request):
    try:
        config = UniversityConfig.get()
        if config.is_setup_complete:
            return redirect('admission:home')
    except:
        pass
    return redirect('setup:wizard')

def setup_wizard(request, step=1):
    try:
        config = UniversityConfig.get()
        if config.is_setup_complete:
            return redirect('admission:home')
    except:
        config = None
    
    if request.method == 'POST':
        save_step_data(request, step, config)
        
        if step < 7:
            return redirect('setup:wizard_step', step=step + 1)
        else:
            config.is_setup_complete = True
            config.setup_completed_at = timezone.now()
            config.save()
            return redirect('setup:complete')
    
    context = {
        'step': step,
        'progress': int((step / 7) * 100),
        'config': config,
    }
    return render(request, f'setup/step_{step}.html', context)

def save_step_data(request, step, config):
    if step == 1:
        config.name = request.POST.get('name', config.name)
        config.short_name = request.POST.get('short_name', config.short_name)
        config.state = request.POST.get('state', config.state)
        config.primary_color = request.POST.get('primary_color', config.primary_color)
        config.secondary_color = request.POST.get('secondary_color', config.secondary_color)
    elif step == 2:
        config.indigene_verification_required = request.POST.get('indigene_verification_required') == 'on'
        config.indigene_verification_fee = request.POST.get('indigene_verification_fee', 5000)
    elif step == 3:
        config.screening_fee_indigene = request.POST.get('screening_fee_indigene', 2000)
        config.screening_fee_non_indigene = request.POST.get('screening_fee_non_indigene', 5000)
        config.service_charge = request.POST.get('service_charge', 3000)
    elif step == 4:
        config.acceptance_fee = request.POST.get('acceptance_fee', 25000)
        config.medical_fee = request.POST.get('medical_fee', 5000)
    elif step == 5:
        config.min_jamb_score = request.POST.get('min_jamb_score', 180)
        config.min_olevel_credits = request.POST.get('min_olevel_credits', 5)
        config.indigene_bonus_points = request.POST.get('indigene_bonus_points', 10)
    elif step == 6:
        import json
        config.deadline_policy = {
            'application_deadline': request.POST.get('application_deadline', ''),
            'screening_deadline': request.POST.get('screening_deadline', ''),
        }
    
    config.save()

def setup_complete(request):
    return render(request, 'setup/complete.html')
