from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Productos

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        Model=Productos
        fields=['descripcion', 'marca', 'serie', 'precio', 'cantidad', 'disponible',]