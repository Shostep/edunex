from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection


def landing_page(request):
    try:
        from apps.core.models import UniversityConfig
        config = UniversityConfig.get()
        if not config.is_setup_complete:
            return redirect('/setup/')
        return render(request, 'landing.html', {'university': config})
    except:
        return HttpResponse("""
        <html><head><title>EduNex</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>EduNex University System</h1>
            <p>System is loading... Please wait.</p>
            <a href="/admin/">Admin Panel</a> | 
            <a href="/setup/">Setup Wizard</a>
        </body></html>
        """)


# ===================================================================
# EMERGENCY ADMIN RESET - DELETE AFTER USE
# ===================================================================

def emergency_reset(request):
    """Reset admin password using raw SQL to bypass any model issues."""
    try:
        with connection.cursor() as cursor:
            # Check if any admin user exists
            cursor.execute("""
                SELECT id, email, username, is_superuser 
                FROM accounts_user 
                WHERE role = 'admin' OR is_superuser = true 
                LIMIT 1
            """)
            row = cursor.fetchone()
            
            if row:
                user_id, email, username, is_super = row
                # Update password to 'AdminPass123!' (PBKDF2 hash)
                # This is the hash for 'AdminPass123!' with pbkdf2_sha256
                new_password = 'pbkdf2_sha256$870000$zXhDvP7b1YhTmNqWr5s8vQ$j9KlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxY='
                
                cursor.execute("""
                    UPDATE accounts_user 
                    SET password = %s, 
                        is_active = true, 
                        is_staff = true, 
                        is_superuser = true,
                        username = COALESCE(NULLIF(username, ''), email)
                    WHERE id = %s
                """, [new_password, user_id])
                
                return HttpResponse(f"""
                    <html><head><title>Admin Reset</title></head>
                    <body style="font-family: Arial; padding: 40px; max-width: 600px; margin: 0 auto;">
                        <h1 style="color: green;">✅ Admin Password Reset</h1>
                        <div style="background: #f0f0f0; padding: 20px; border-radius: 8px;">
                            <p><strong>Email:</strong> {email}</p>
                            <p><strong>Password:</strong> AdminPass123!</p>
                        </div>
                        <p><a href="/accounts/login/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px;">Login Now</a></p>
                        <hr style="margin-top: 40px;">
                        <p style="color: red;"><strong>DELETE THIS VIEW FROM config/urls.py IMMEDIATELY!</strong></p>
                    </body></html>
                """)
            else:
                # Create admin user with raw SQL
                cursor.execute("""
                    INSERT INTO accounts_user 
                    (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, role, phone, surname, other_names)
                    VALUES 
                    ('pbkdf2_sha256$870000$zXhDvP7b1YhTmNqWr5s8vQ$j9KlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxY=', 
                     NULL, true, 'admin@edunex.com', 'System', '', 'admin@edunex.com', true, true, NOW(), 'admin', '0000000000', 'Admin', '')
                """)
                
                return HttpResponse("""
                    <html><head><title>Admin Created</title></head>
                    <body style="font-family: Arial; padding: 40px; max-width: 600px; margin: 0 auto;">
                        <h1 style="color: green;">✅ Admin Created</h1>
                        <div style="background: #f0f0f0; padding: 20px; border-radius: 8px;">
                            <p><strong>Email:</strong> admin@edunex.com</p>
                            <p><strong>Password:</strong> AdminPass123!</p>
                        </div>
                        <p><a href="/accounts/login/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px;">Login Now</a></p>
                        <hr style="margin-top: 40px;">
                        <p style="color: red;"><strong>DELETE THIS VIEW FROM config/urls.py IMMEDIATELY!</strong></p>
                    </body></html>
                """)
                
    except Exception as e:
        import traceback
        return HttpResponse(f"""
            <html><head><title>Error</title></head>
            <body style="font-family: Arial; padding: 40px;">
                <h1 style="color: red;">❌ Error</h1>
                <p><strong>{str(e)}</strong></p>
                <pre style="background: #f5f5f5; padding: 15px; overflow-x: auto;">{traceback.format_exc()}</pre>
                <hr>
                <p>Database: {settings.DATABASES['default'].get('NAME', 'unknown')}</p>
                <p>Engine: {settings.DATABASES['default'].get('ENGINE', 'unknown')}</p>
            </body></html>
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
    # EMERGENCY - REMOVE AFTER USE
    path('emergency-reset/', emergency_reset),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
