from django.shortcuts import render, redirect, get_object_or_404
from taller.models import Mueble, Categoria
from taller.forms import MuebleForm

def mueble_list(request):
    pista = request.GET.get('pista', '').strip()
    categoria_id = request.GET.get('categoria_id', '').strip()
    muebles = Mueble.objects.select_related('categoria').all()
    if pista:
        muebles = muebles.filter(nombre__icontains=pista)
    if categoria_id:
        muebles = muebles.filter(categoria_id=categoria_id)
    return render(request, 'taller/mueble_list.html', {
        'muebles': muebles,
        'categorias': Categoria.objects.all(),
        'pista': pista,
        'categoria_id': categoria_id,
    })

def mueble_create(request):
    if request.method == 'POST':
        form = MuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mueble_list')
    else:
        form = MuebleForm()
    return render(request, 'taller/formulario.html', {'form': form})

def mueble_update(request, pk):
    mueble = get_object_or_404(Mueble, pk=pk)
    if request.method == 'POST':
        form = MuebleForm(request.POST, instance=mueble)
        if form.is_valid():
            form.save()
            return redirect('mueble_list')
    else:
        form = MuebleForm(instance=mueble)
    return render(request, 'taller/formulario.html', {'form': form})

def mueble_delete(request, pk):
    mueble = get_object_or_404(Mueble, pk=pk)
    if request.method == 'POST':
        mueble.delete()
        return redirect('mueble_list')
    return render(request, 'taller/confirm_delete.html', {'objeto': mueble})