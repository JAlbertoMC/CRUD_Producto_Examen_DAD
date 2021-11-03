from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serialiazers import ProductoSerializer
from .models import Productos

class ProductoViewSet (viewsets.ModelViewSet):
    queryset=Productos.objects.all()
    serializers_class=ProductoSerializer

class ProductolistarSet (viewsets.ModelViewSet):
    queryset=Productos.objects.all()
    serializers_class=ProductoSerializer
