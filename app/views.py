# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Product
from django.shortcuts import render
from rest_framework import viewsets
from serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
