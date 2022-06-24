from dataclasses import field
from statistics import mode
from rest_framework.serializers import ModelSerializer

from .models import Category, Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'description', 'price', 'get_image', 'get_thumnail', 'date_added', 'get_absolute_url')