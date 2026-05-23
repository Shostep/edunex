from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.http import HttpResponse

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
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
