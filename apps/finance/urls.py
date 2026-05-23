from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.bursar_dashboard, name='dashboard'),
    path('fee-structure/', views.fee_structure, name='fee_structure'),
    path('payments/', views.payment_records, name='payments'),
    path('reports/', views.financial_reports, name='reports'),
    path('receipts/', views.receipts, name='receipts'),
    path('balances/', views.outstanding_balances, name='balances'),
]
