from .views import ProductListAPIView
from django.urls import path

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name='products')
]
