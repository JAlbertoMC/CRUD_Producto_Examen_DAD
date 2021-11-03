from django.db import models

class Productos(models.Model):

    descripcion=models.CharField(max_length=250)
    marca=models.CharField(max_length=50, null=True)
    serie=models.CharField(max_length=20)
    precio=models.CharField(max_length=20, null=True)
    cantidad=models.CharField(max_length=50)
    disponible=models.CharField(max_length=50,)

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.descripcion
