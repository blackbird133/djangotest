from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from returnbook.models import ReturnedBook
from returnbook.serializers import ReturnBookListSerializer, ReturnBookDetailSerializer


class ReturnBookListViewSet(generics.ListCreateAPIView):
    queryset = ReturnedBook.objects.all()
    serializer_class = ReturnBookListSerializer


class ReturnBookDetailViewSet(generics.RetrieveAPIView):
    queryset = ReturnedBook.objects.all()
    serializer_class = ReturnBookDetailSerializer
