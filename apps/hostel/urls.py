from django.urls import path
from . import views

app_name = 'hostel'

urlpatterns = [
    path('', views.hostel_dashboard, name='dashboard'),
    path('rooms/', views.room_management, name='rooms'),
    path('allocate/', views.allocate_student, name='allocate'),
    path('allocations/', views.view_allocations, name='allocations'),
]
