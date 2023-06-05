from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from book.models import BooksModel
from book.serializers import BookListSerializers, BookDetailSerializer


class BookListViewSet(generics.ListAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookListSerializers


class BookDetailViewSet(generics.RetrieveAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
