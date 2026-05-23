from django.urls import path
from . import views

app_name = 'medical'

urlpatterns = [
    path('', views.medical_dashboard, name='dashboard'),
    path('records/', views.student_records, name='records'),
    path('appointments/', views.appointments, name='appointments'),
]
