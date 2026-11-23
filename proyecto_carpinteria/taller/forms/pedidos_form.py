from django import forms

from taller.models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'mueble', 'cantidad', 'estado', 'observaciones']
