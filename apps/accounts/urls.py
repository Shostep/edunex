from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import EmailPasswordResetForm  # We'll create this

app_name = 'accounts'

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        form_class=EmailPasswordResetForm,
        success_url='/accounts/password-reset/done/'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('create-admin/', views.create_first_admin, name='create_admin'),
]
