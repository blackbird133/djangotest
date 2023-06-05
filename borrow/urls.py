from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "book"
router = routers.DefaultRouter()
router.register(r'borrow',views.BorrowListViewSet)

urlpatterns = [
    path('', views.BorrowListViewSet.as_view(), name="borrow-book-list"),
    path('<int:pk>/"', views.BorrowDetailViewSet.as_view(), name="borrow-book-detail")
]