from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from .categoria import Categoria
from .cliente import Cliente


class Mueble(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='muebles',
    )
    clientes = models.ManyToManyField(
        Cliente,
        through='Pedido',
        through_fields=('mueble', 'cliente'),
        related_name='muebles_interesados',
        blank=True,
    )
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='muebles_creados',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = 'mueble'
        verbose_name_plural = 'muebles'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('mueble_detail', args=[self.pk])