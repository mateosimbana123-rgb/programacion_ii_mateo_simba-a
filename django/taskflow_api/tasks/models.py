# tasks/models.py
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Nave (models. Model):
    nombre = models.CharField(max_length=100)
    tipo_nave = models.TextField(blank=True)
    combustible = models.TextField(blank=True)
    created_at = models. DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Comida (models.Model):
    nombre_comida = models. CharField(max_length=100)
    categoria = models.TextField(blank=True)
    ingredientes = models. TextField(blank=True)
    created_at = models. DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nombre_comida

class Carpinteria(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
