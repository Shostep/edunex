# library - views.py
from django.shortcuts import render

def library_dashboard(request):
    return render(request, 'library/dashboard.html')

def book_catalog(request):
    return render(request, 'library/catalog.html')

def issue_book(request):
    return render(request, 'library/issue.html')

def process_returns(request):
    return render(request, 'library/returns.html')

def overdue_books(request):
    return render(request, 'library/overdue.html')
