
import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from product.models import Product, Category
from .serializers import OrderSerializer 
# Create your views here.


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_API_KEY
        paid_amount = sum(item.get('quantity') * item.get('price') for item in serializer.validated_data.get('items'))
        try:
            charge = stripe.Charge.create(
                amount=paid_amount,
                currency="usd",
                description="My First Test Charge (created for API docs at https://www.stripe.com/docs/api)",
                source=serializer.validated_data.get('stripe_token'), # obtained with Stripe.js
            )

            serializer.save(user=request.User, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as exc:
            print(exc)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)