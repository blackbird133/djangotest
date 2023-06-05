from django.contrib import admin
from .models import ReturnedBook


@admin.register(ReturnedBook)
class ReturnedBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'borrowID', 'returnDate', 'isApproved']
