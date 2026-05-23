from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()


def landing_page(request):
    try:
        from apps.core.models import UniversityConfig
        config = UniversityConfig.get()
        if not config.is_setup_complete:
            return redirect('/setup/')
        return render(request, 'landing.html', {'university': config})
    except:
        return HttpResponse("""
        <html>
        <head><title>EduNex</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>EduNex University System</h1>
            <p>System is loading... Please wait.</p>
            <a href="/admin/">Admin Panel</a> | 
            <a href="/setup/">Setup Wizard</a>
        </body>
        </html>
        """)


# ===================================================================
# EMERGENCY ADMIN RESET - DELETE THIS AFTER REGAINING ACCESS
# ===================================================================

def emergency_reset(request):
    """Reset or create admin user. Visit /emergency/ to use."""
    try:
        user = User.objects.filter(role='admin').first()
        
        if user:
            # Fix existing admin
            user.username = user.email
            user.set_password('AdminPass123!')
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            return HttpResponse(f"""
                <h1>✅ Admin Password Reset</h1>
                <p><strong>Email:</strong> {user.email}</p>
                <p><strong>Password:</strong> AdminPass123!</p>
                <p><a href="/accounts/login/">Login Now</a></p>
                <hr>
                <p style="color:red"><strong>DELETE THE emergency_reset VIEW FROM config/urls.py IMMEDIATELY!</strong></p>
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
                <h1>✅ Admin Created</h1>
                <p><strong>Email:</strong> admin@edunex.com</p>
                <p><strong>Password:</strong> AdminPass123!</p>
                <p><a href="/accounts/login/">Login Now</a></p>
                <hr>
                <p style="color:red"><strong>DELETE THE emergency_reset VIEW FROM config/urls.py IMMEDIATELY!</strong></p>
            """)
    except Exception as e:
        return HttpResponse(f"<h1>❌ Error</h1><p>{str(e)}</p><p>Check database connection.</p>")


def emergency_fix_users(request):
    """Fix users with empty username fields. Visit /emergency-fix/ to use."""
    try:
        fixed = 0
        for user in User.objects.filter(username=''):
            user.username = user.email
            user.save()
            fixed += 1
        return HttpResponse(f"""
            <h1>✅ Fixed {fixed} Users</h1>
            <p>Users with empty username fields have been updated.</p>
            <p><a href="/accounts/login/">Go to Login</a></p>
            <hr>
            <p style="color:red"><strong>DELETE THIS VIEW FROM config/urls.py IMMEDIATELY!</strong></p>
        """)
    except Exception as e:
        return HttpResponse(f"<h1>❌ Error</h1><p>{str(e)}</p>")


# ===================================================================

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing'),
    path('setup/', include('apps.setup_wizard.urls')),
    path('indigene/', include('apps.indigene.urls')),
    path('apply/', include('apps.admission.urls')),
    path('student/', include('apps.students.urls')),
    path('lecturer/', include('apps.lecturers.urls')),
    path('examination/', include('apps.examination.urls')),
    path('finance/', include('apps.finance.urls')),
    path('hostel/', include('apps.hostel.urls')),
    path('medical/', include('apps.medical.urls')),
    path('library/', include('apps.library.urls')),
    path('alumni/', include('apps.alumni.urls')),
    path('payments/', include('apps.payments.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('academics/', include('apps.academics.urls')),
    # EMERGENCY URLS - REMOVE AFTER USE
    path('emergency/', emergency_reset),
    path('emergency-fix/', emergency_fix_users),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
