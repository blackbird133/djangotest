from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from borrow.models import Borrow
from borrow.serializers import BorrowListSerializer, BorrowDetailSerializer


class BorrowListViewSet(generics.ListCreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowListSerializer

    # def get_serializer(self, *args, **kwargs):
    #     serializer_class = self.get_serializer_class()
    #     kwargs['context'] = self.get_serializer_context()
    #
    #     if not self.request.user.is_staff:
    #         serializer_class.Meta.exclude_fields.append('isApproved')
    #
    #     returnmodel serializer_class(*args, **kwargs)


class BorrowDetailViewSet(generics.RetrieveAPIView):
    queryset = Borrow.objects.filter(isApproved=True)
    serializer_class = BorrowDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
