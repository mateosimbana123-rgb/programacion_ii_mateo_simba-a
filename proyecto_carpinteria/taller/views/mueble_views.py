from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from taller.forms import MuebleForm
from taller.models import Categoria, Mueble


def mueble_list(request):
    pista = request.GET.get('pista', '').strip()
    categoria_id = request.GET.get('categoria_id', '').strip()
    muebles = Mueble.objects.select_related('categoria').all()
    if pista:
        muebles = muebles.filter(nombre__icontains=pista)
    if categoria_id:
        muebles = muebles.filter(categoria_id=categoria_id)
    return render(request, 'taller/muebles/mueble_list.html', {
        'muebles': muebles,
        'categorias': Categoria.objects.all(),
        'pista': pista,
        'categoria_id': categoria_id,
    })


def mueble_detail(request, pk):
    mueble = get_object_or_404(Mueble.objects.select_related('categoria'), pk=pk)
    return render(request, 'taller/muebles/mueble_detail.html', {'mueble': mueble})


@login_required
@permission_required('taller.add_mueble', raise_exception=True)
def mueble_create(request):
    form = MuebleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        mueble = form.save(commit=False)
        mueble.creado_por = request.user
        mueble.save()
        messages.success(request, 'Mueble creado exitosamente.')
        return redirect('mueble_list')
    return render(request, 'taller/muebles/formulario.html', {'form': form})


@login_required
@permission_required('taller.change_mueble', raise_exception=True)
def mueble_update(request, pk):
    mueble = get_object_or_404(Mueble, pk=pk)
    if not request.user.groups.filter(name='administradores').exists() and mueble.creado_por != request.user:
        raise PermissionDenied
    form = MuebleForm(request.POST or None, instance=mueble)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Mueble actualizado exitosamente.')
        return redirect('mueble_list')
    return render(request, 'taller/muebles/formulario.html', {'form': form})


@login_required
@permission_required('taller.delete_mueble', raise_exception=True)
def mueble_delete(request, pk):
    mueble = get_object_or_404(Mueble, pk=pk)
    if not request.user.groups.filter(name='administradores').exists() and mueble.creado_por != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        mueble.delete()
        messages.success(request, 'Mueble eliminado exitosamente.')
        return redirect('mueble_list')
    return render(request, 'taller/muebles/confirm_delete.html', {'objeto': mueble})