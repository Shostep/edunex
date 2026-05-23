from django.contrib import admin
from .models import Book, BookIssue

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'available_copies', 'is_active']
    search_fields = ['title', 'author', 'isbn']

@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):
    list_display = ['book', 'student', 'status', 'due_date', 'fine_amount']
    list_filter = ['status', 'due_date']
