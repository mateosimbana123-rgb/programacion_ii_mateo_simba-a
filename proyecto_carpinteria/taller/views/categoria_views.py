from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from taller.forms import CategoriaForm
from taller.models import Categoria


def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'taller/categorias/categoria_list.html', {'categorias': categorias})


def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'taller/categorias/categoria_detail.html', {'categoria': categoria})


@login_required
@permission_required('taller.add_categoria', raise_exception=True)
def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoría creada exitosamente.')
        return redirect('categoria_list')
    return render(request, 'taller/categorias/formulario.html', {'form': form})


@login_required
@permission_required('taller.change_categoria', raise_exception=True)
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoría actualizada exitosamente.')
        return redirect('categoria_list')
    return render(request, 'taller/categorias/formulario.html', {'form': form})


@login_required
@permission_required('taller.delete_categoria', raise_exception=True)
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('categoria_list')
    return render(request, 'taller/categorias/confirm_delete.html', {'objeto': categoria})
