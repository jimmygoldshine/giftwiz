# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Product
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'products': reverse('products:product-list', request=request, format=format)
    })

@api_view(['GET'])
def product_list(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=true)
    return Response(serializer.data)
