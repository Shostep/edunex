from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


def custom_login(request):
    """Custom login view using email as the username field."""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # FIX: Use 'email=' keyword since USERNAME_FIELD = 'email'
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.email}!')
            return redirect('/admin/')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'accounts/login.html')


def create_first_admin(request):
    """Temporary view to create the first admin user."""
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
            # FIX: Pass username=email since AbstractUser requires a username field
            user = User.objects.create_superuser(
                email=email,           # USERNAME_FIELD
                password=password,
                phone=phone,
                surname=surname,
                first_name=first_name,
                username=email,        # REQUIRED: AbstractUser username field
            )
            user.role = 'admin'
            # create_superuser already sets is_staff=True and is_superuser=True
            user.save()
            
            messages.success(request, 'Admin account created successfully! Please login.')
            return redirect('accounts:login')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
    
    return render(request, 'accounts/create_admin.html')
