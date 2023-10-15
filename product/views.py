from rest_framework import generics
# from rest_framework import permissions
from .serilizers import ProductSerializer
from .models import Product


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
