from typing import Any
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, CartSerializer, CartItemSerialzer
from .models import Product, Cart, CartItem
from django.views.generic import ListView
from rest_framework import mixins

class ProductListByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category__id=category_id)

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartRetrieveAPIView(generics.ListAPIView):
    serializer_class = CartItemSerialzer

    def get_queryset(self):
        # Assuming you have an authenticated user making the request
        customer = self.request.user.customer
        try:
            cart = customer.cart
            return CartItem.objects.filter(cart=cart)
        except Cart.DoesNotExist:
            return CartItem.objects.none()