from . import models
from rest_framework import serializers


class BorrowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Borrow
        fields = ['id', 'bookID', 'borrowBy', 'isApproved']


class BorrowDetailSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Borrow
        fields = ['id', 'bookID', 'borrowBy', 'borrowDate', 'returnException', 'isApproved']