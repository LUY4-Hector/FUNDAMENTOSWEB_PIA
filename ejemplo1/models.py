from django.db import models

# Create your models here.
class Departamento(models.Model):
    clave = models.CharField(max_length=10) # Agregar descripcion de la funcion
    nombre = models.CharField(max_length=50) # Agregar descripcion de la funcion

