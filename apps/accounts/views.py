from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.email}!')
            return redirect('/admin/')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'accounts/login.html')

def create_first_admin(request):
    """Temporary view to create the first admin user"""
    # Check if any admin already exists
    if User.objects.filter(role='admin').exists():
        messages.info(request, 'Admin user already exists. Please login.')
        return redirect('accounts:login')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        surname = request.POST.get('surname')
        first_name = request.POST.get('first_name')
        phone = request.POST.get('phone')
        
        try:
            # FIXED: Don't pass username=email if USERNAME_FIELD is already 'email'
            # create_superuser expects the USERNAME_FIELD as the first argument
            user = User.objects.create_superuser(
                email=email,           # This is the USERNAME_FIELD
                password=password,
                phone=phone,
                surname=surname,
                first_name=first_name,
                # Removed: username=email
            )
            user.role = 'admin'
            user.is_staff = True
            user.is_superuser = True
            user.save()
            
            messages.success(request, 'Admin account created successfully! Please login.')
            return redirect('accounts:login')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
    
    return render(request, 'accounts/create_admin.html')
