from dataclasses import field
from operator import mod
from statistics import mode
from rest_framework.serializers import ModelSerializer

from .models import Category, Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'description', 'price', 'get_image', 'get_thumnail', 'date_added', 'get_absolute_url')


class CategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'products',
        )