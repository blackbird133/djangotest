from django.contrib import admin

from .models import BooksModel


@admin.register(BooksModel)
class BooksModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'bookTitle', 'bookCategory', 'isAvailable']
    search_fields = ['bookCategory', 'isAvailable']
