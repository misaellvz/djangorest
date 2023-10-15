from rest_framework import serializers
from .models import Category, Product, Image
from .fields import HttpBase64ImageField


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    photo = HttpBase64ImageField()

    class Meta:
        model = Image
        fields = ['id', 'photo']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'status', 'categories', 'images']
