from django.urls import path
from . import views

app_name = 'alumni'

urlpatterns = [
    path('', views.alumni_dashboard, name='dashboard'),
    path('transcript/', views.alumni_transcript, name='transcript'),
    path('certificate/', views.certificate_verification, name='certificate'),
    path('verify/<str:cert_id>/', views.public_verify_certificate, name='public_verify'),
]
