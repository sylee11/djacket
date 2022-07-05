from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Order, OrderItem
from product.serializers import ProductSerializer


class OrderItemSerializer(ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        field = (
            'product'
            'price',
            'quantity'
        )

class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        field = (
            'id',
            'user',
            'first_name',
            'last_name',
            'email',
            'address',
            'zipcode',
            'place',
            'phone',
            'paid_amount',
            'stripe_token',
            'created_at',
            'items'
        )
    
    def create(self, validated_data):
        item_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in item_data:
            OrderItem.objects.create(order=order, **item)
        
        return order