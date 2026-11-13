from django.shortcuts import render, redirect
from django.contrib import messages
from catalogo.forms import AutorForm
from catalogo.models import Autor
from django.contrib.h.decorators import login_required, permission_required

@login_required
@permission_required('catalogo.view_Autor', raise_exception=True)
def Autor_list(request):
    Autores = Autor.objects.all()
    return render(request, 'Autor_list.html', 
                    {'Autores': Autores})

@login_required
@permission_required('catalogo.add_Autor', raise_exception=True)
def Autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('Autor_list')
    else:
        form = AutorForm()
    return render(request, 
                    'catalogo/Autores/formulario.html', 
                    {'form': form})

@login_required
@permission_required('catalogo.change_Autor', raise_exception=True)
def Autor_update(request, pk):
    Autor = Autor.objects.get(pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=Autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('Autor_list')
    else:
        form = AutorForm(instance=Autor)
    return render(request, 
                    'catalogo/Autores/formulario.html', 
                    {'form': form})

@login_required
@permission_required('catalogo.delete_Autor', raise_exception=True)
def Autor_delete(request, pk):
    Autor = Autor.objects.get(pk=pk)
    if request.method == 'POST':
        Autor.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('Autor_list')
    return render(request, 
                    'catalogo/Autores/Autor_confirm_delete.html', 
                    {'Autor': Autor})