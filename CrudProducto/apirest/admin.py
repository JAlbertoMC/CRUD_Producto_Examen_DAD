from django.contrib import admin
from .models import Productos


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'marca', 'serie', 'precio', 'cantidad', 'disponible',)

admin.site.register(Productos, ProductoAdmin)

