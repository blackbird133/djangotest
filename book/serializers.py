from rest_framework import serializers

from . import models


class BookListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.BooksModel
        fields = ['id', 'bookTitle', 'bookCategory', "description", "isAvailable"]


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BooksModel
        fields = ['id', 'bookTitle', 'bookCategory', 'description', 'created', 'isAvailable' ]
