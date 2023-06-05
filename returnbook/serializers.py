from . import models
from rest_framework import serializers


class ReturnBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReturnedBook
        fields = ['id', 'borrowID']


class ReturnBookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReturnedBook
        fields = ['id', 'borrowID', 'returnDate', 'isApproved']
