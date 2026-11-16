from django.shortcuts import render, redirect, get_object_or_404
from taller.models import Mueble
from taller.forms import MuebleForm

def mueble_list(request):
    muebles = Mueble.objects.all()
    return render(request, 'taller/mueble_list.html', {'muebles': muebles})

def mueble_create(request):
    if request.method == 'POST':
        form = MuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mueble_list')
    else:
        form = MuebleForm()
    return render(request, 'taller/formulario.html', {'form': form})