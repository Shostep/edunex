from django.urls import path
from . import views

app_name = 'setup'

urlpatterns = [
    path('', views.redirect_to_setup, name='redirect'),
    path('wizard/', views.setup_wizard, name='wizard'),
    path('wizard/<int:step>/', views.setup_wizard, name='wizard_step'),
    path('complete/', views.setup_complete, name='complete'),
]
