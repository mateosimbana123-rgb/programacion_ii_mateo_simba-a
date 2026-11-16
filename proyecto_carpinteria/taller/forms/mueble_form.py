from django import forms
from taller.models import Mueble

class MuebleForm(forms.ModelForm):
    class Meta:
        model = Mueble
        fields = ['nombre', 'descripcion', 'precio', 'stock']