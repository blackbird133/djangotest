from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "returnbook"
router = routers.DefaultRouter()
router.register(r'returnbook', views.ReturnBookListViewSet)

urlpatterns = [
    path('', views.ReturnBookListViewSet.as_view(), name="return-book-list"),
    path('<int:pk>/"', views.ReturnBookDetailViewSet.as_view(), name="return-book-detail")
]