from django.db import models

# Create your models here.

class Formulario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    id_mascota = models.CharField(max_length=100)



