from django.contrib import admin
from .models import Borrow


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ['id', 'borrowBy', 'borrowDate', 'isApproved']
    readonly_fields = ['bookID']

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not request.user.is_staff:
            fields = tuple(field for field in fields if field != 'isApproved')
        return fields
