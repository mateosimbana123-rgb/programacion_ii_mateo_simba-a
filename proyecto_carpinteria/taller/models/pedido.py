from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from .cliente import Cliente
from .mueble import Mueble


class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        EN_PROCESO = 'en_proceso', 'En proceso'
        ENTREGADO = 'entregado', 'Entregado'
        CANCELADO = 'cancelado', 'Cancelado'

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='pedidos',
    )
    mueble = models.ForeignKey(
        Mueble,
        on_delete=models.PROTECT,
        related_name='pedidos',
    )
    cantidad = models.PositiveIntegerField(default=1)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )
    fecha_pedido = models.DateField(auto_now_add=True)
    observaciones = models.TextField(blank=True)
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='pedidos_creados',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-fecha_pedido']
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return f"Pedido #{self.pk} - {self.cliente}"

    def get_absolute_url(self):
        return reverse('pedido_detail', args=[self.pk])
