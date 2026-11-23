from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from catalogo.forms import AutorForm
from catalogo.models import Autor


@login_required
@permission_required('catalogo.view_autor', raise_exception=True)
def Autor_list(request):
    pista = request.GET.get('pista', '').strip()
    autores = Autor.objects.all()
    if pista:
        autores = autores.filter(
            Q(nombre__icontains=pista) | Q(apellido__icontains=pista)
        )
    return render(request, 'autores/autor_list.html', {
        'autores': autores,
        'pista': pista,
    })


@login_required
@permission_required('catalogo.add_autor', raise_exception=True)
def Autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado exitosamente.')
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'autores/formulario.html', {'form': form})


@login_required
@permission_required('catalogo.change_autor', raise_exception=True)
def Autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor actualizado exitosamente.')
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autores/formulario.html', {'form': form})


@login_required
@permission_required('catalogo.delete_autor', raise_exception=True)
def Autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'Autor eliminado exitosamente.')
        return redirect('autor_list')
    return render(request, 'autores/autor_confirm_delete.html', {
        'autor': autor,
    })
