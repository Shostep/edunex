from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse

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
            user.save()
            
            messages.success(request, 'Admin account created successfully! Please login.')
            return redirect('accounts:login')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
    
    return render(request, 'accounts/create_admin.html')


# ===================================================================
# TEMPORARY EMERGENCY VIEWS - DELETE THESE AFTER REGAINING ACCESS
# ===================================================================

def emergency_reset_admin(request):
    """
    EMERGENCY: Reset or create admin via browser.
    URL: /emergency-reset/
    DELETE THIS VIEW AFTER USE - IT HAS NO AUTHENTICATION
    """
    try:
        # Try to find existing admin
        user = User.objects.filter(role='admin').first()
        
        if user:
            # Reset existing admin
            user.username = user.email
            user.set_password('AdminPass123!')
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            return HttpResponse(f"""
                <h1>Admin Password Reset</h1>
                <p>Email: {user.email}</p>
                <p>New Password: AdminPass123!</p>
                <p><a href="/accounts/login/">Login Now</a></p>
                <hr>
                <p style="color:red"><strong>DELETE THIS VIEW FROM accounts/views.py IMMEDIATELY!</strong></p>
            """)
        else:
            # Create new admin
            user = User.objects.create_superuser(
                email='admin@edunex.com',
                password='AdminPass123!',
                username='admin@edunex.com',
                phone='0000000000',
                surname='Admin',
                first_name='System',
            )
            user.role = 'admin'
            user.save()
            return HttpResponse("""
                <h1>Admin Created</h1>
                <p>Email: admin@edunex.com</p>
                <p>Password: AdminPass123!</p>
                <p><a href="/accounts/login/">Login Now</a></p>
                <hr>
                <p style="color:red"><strong>DELETE THIS VIEW FROM accounts/views.py IMMEDIATELY!</strong></p>
            """)
    except Exception as e:
        return HttpResponse(f"<h1>Error: {str(e)}</h1><p>Check your database connection.</p>")


def emergency_fix_existing_users(request):
    """
    EMERGENCY: Fix all users who have empty username fields.
    URL: /emergency-fix-users/
    DELETE THIS VIEW AFTER USE
    """
    try:
        fixed_count = 0
        for user in User.objects.filter(username=''):
            user.username = user.email
            user.save()
            fixed_count += 1
        
        return HttpResponse(f"""
            <h1>User Fix Complete</h1>
            <p>Fixed {fixed_count} users with empty username fields.</p>
            <p><a href="/accounts/login/">Go to Login</a></p>
            <hr>
            <p style="color:red"><strong>DELETE THIS VIEW FROM accounts/views.py IMMEDIATELY!</strong></p>
        """)
    except Exception as e:
        return HttpResponse(f"<h1>Error: {str(e)}</h1>")
