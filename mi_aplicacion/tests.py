from django.test import TestCase
from django.db import models

# Create your tests here.

HOMBRE = 2
MUJER = 1
NEUTRO = 0
SEXO = [
    (NEUTRO, "Prefiero no decir"),
    (HOMBRE, 'Hombre'),
    (MUJER, 'Mujer'),
]

class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)

class Maestro(models.Model):
    nombre = models.CharField(max_length=100)
    escuela = models.ForeignKey(Escuela, on_delete=models.PROTECT, null=False)
    sexo = models.IntegerField(choices=SEXO, default=NEUTRO, null=False)
    fecha_nacimiento = models.DateField(null=False)

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    escuela = models.ForeignKey(Escuela, on_delete=models.PROTECT, null=False)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, null=False)
    sexo = models.IntegerField(choices=SEXO, default=NEUTRO, null=False)
    fecha_nacimiento = models.DateField(null=False)
