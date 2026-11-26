from django import forms

from taller.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email', 'direccion']
        widgets = {
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'telefono': forms.TextInput(),
            'email': forms.EmailInput(),
            'direccion': forms.TextInput(),
        }

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono'].strip()
        if len(telefono) < 7:
            raise forms.ValidationError('Ingrese un teléfono válido.')
        return telefono
