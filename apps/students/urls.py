from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_dashboard, name='dashboard'),
    path('courses/', views.course_registration, name='course_reg'),
    path('results/', views.view_results, name='results'),
    path('fees/', views.view_fees, name='fees'),
    path('transcript/', views.request_transcript, name='transcript'),
    path('timetable/', views.view_timetable, name='timetable'),
    path('hostel/', views.hostel_application, name='hostel'),
    path('medical/', views.medical_dashboard, name='medical'),
    path('library/', views.library_dashboard, name='library'),
    path('id-card/', views.id_card, name='id_card'),
    path('profile/', views.student_profile, name='profile'),
]
