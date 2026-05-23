from django.urls import path
from . import views

app_name = 'admission'

urlpatterns = [
    # Public
    path('', views.admission_home, name='home'),
    path('list/', views.public_admission_list, name='public_list'),
    path('verify/', views.verify_admission, name='verify'),

    # Application flow
    path('start/<int:session_id>/', views.start_application, name='start'),
    path('<int:app_id>/personal/', views.step_personal, name='step_personal'),
    path('<int:app_id>/academic/', views.step_academic, name='step_academic'),
    path('<int:app_id>/payment/', views.step_payment, name='step_payment'),
    path('payment/callback/', views.payment_callback, name='payment_callback'),
    path('<int:app_id>/upload/', views.step_upload, name='step_upload'),
    path('<int:app_id>/tracker/', views.application_tracker, name='tracker'),

    # Admission response
    path('<int:app_id>/respond/', views.respond_to_admission, name='respond'),
    path('<int:app_id>/acceptance/', views.pay_acceptance_fee, name='pay_acceptance'),
    path('acceptance/callback/', views.acceptance_callback, name='acceptance_callback'),

    # Admin
    path('admin/screening/', views.admin_screening_dashboard, name='admin_screening'),
    path('admin/verify/<int:app_id>/<str:doc_type>/', views.admin_verify_document, name='admin_verify_doc'),
    path('admin/screen/<int:app_id>/', views.admin_manual_screen, name='admin_manual_screen'),
    path('admin/publish/', views.publish_admission_list, name='publish_list'),
]
