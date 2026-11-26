from django import forms

from taller.models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'mueble', 'cantidad', 'estado', 'observaciones']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': '1'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 1:
            raise forms.ValidationError('La cantidad debe ser mayor que cero.')
        return cantidad
