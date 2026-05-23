from django.urls import path
from . import views

app_name = 'indigene'

urlpatterns = [
    path('', views.indigene_home, name='home'),
    path('apply/', views.apply_indigene, name='apply'),
    path('upload/<int:app_id>/', views.upload_indigene_docs, name='upload'),
    path('pay/<int:app_id>/', views.pay_indigene_fee, name='pay'),
    path('status/<int:app_id>/', views.indigene_status, name='status'),
    path('tracker/<int:app_id>/', views.indigene_tracker, name='tracker'),
]
