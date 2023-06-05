from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "book"
router = routers.DefaultRouter()
router.register(r'book',views.BookListViewSet)

urlpatterns = [
    path('', views.BookListViewSet.as_view(), name="book-list"),
    path('<int:pk>/"', views.BookDetailViewSet.as_view(), name="book-detail")
]