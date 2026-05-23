from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import django

# Setup Django settings for model access
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

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
# EMERGENCY ADMIN RESET - DELETE AFTER REGAINING ACCESS
# ===================================================================

def emergency_reset(request):
    """Reset or create admin user."""
    try:
        # Check if any admin exists
        admin_users = User.objects.filter(role='admin')
        
        if admin_users.exists():
            user = admin_users.first()
            # Reset password and ensure username matches email
            user.username = user.email
            user.set_password('AdminPass123!')
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            
            return HttpResponse(f"""
                <html>
                <head><title>Admin Reset</title></head>
                <body style="font-family: Arial; padding: 40px; max-width: 600px; margin: 0 auto;">
                    <h1 style="color: green;">✅ Admin Password Reset</h1>
                    <div style="background: #f0f0f0; padding: 20px; border-radius: 8px;">
                        <p><strong>Email:</strong> {user.email}</p>
                        <p><strong>Password:</strong> AdminPass123!</p>
                    </div>
                    <p><a href="/accounts/login/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px;">Login Now</a></p>
                    <hr style="margin-top: 40px;">
                    <p style="color: red;"><strong>SECURITY WARNING:</strong> Delete the emergency_reset view from config/urls.py immediately after logging in!</p>
                </body>
                </html>
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
                <html>
                <head><title>Admin Created</title></head>
                <body style="font-family: Arial; padding: 40px; max-width: 600px; margin: 0 auto;">
                    <h1 style="color: green;">✅ Admin Created</h1>
                    <div style="background: #f0f0f0; padding: 20px; border-radius: 8px;">
                        <p><strong>Email:</strong> admin@edunex.com</p>
                        <p><strong>Password:</strong> AdminPass123!</p>
                    </div>
                    <p><a href="/accounts/login/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px;">Login Now</a></p>
                    <hr style="margin-top: 40px;">
                    <p style="color: red;"><strong>SECURITY WARNING:</strong> Delete the emergency_reset view from config/urls.py immediately after logging in!</p>
                </body>
                </html>
            """)
    except Exception as e:
        import traceback
        return HttpResponse(f"""
            <html>
            <head><title>Error</title></head>
            <body style="font-family: Arial; padding: 40px;">
                <h1 style="color: red;">❌ Error</h1>
                <p>{str(e)}</p>
                <pre style="background: #f5f5f5; padding: 15px; overflow-x: auto;">{traceback.format_exc()}</pre>
            </body>
            </html>
        """)


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
    # EMERGENCY URL - REMOVE AFTER USE
    path('emergency-reset/', emergency_reset),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
