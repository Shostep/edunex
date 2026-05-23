from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.library_dashboard, name='dashboard'),
    path('catalog/', views.book_catalog, name='catalog'),
    path('issue/', views.issue_book, name='issue'),
    path('returns/', views.process_returns, name='returns'),
    path('overdue/', views.overdue_books, name='overdue'),
]
