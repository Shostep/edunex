from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Try to authenticate
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name() or user.email}!')
            
            # Redirect based on role
            if user.role == 'student':
                return redirect('students:dashboard')
            elif user.role == 'lecturer':
                return redirect('lecturers:dashboard')
            elif user.role == 'admin':
                return redirect('admin:index')
            else:
                return redirect('landing')
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'accounts/login.html')
