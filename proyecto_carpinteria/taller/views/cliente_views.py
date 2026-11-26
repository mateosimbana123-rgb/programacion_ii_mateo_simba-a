from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from taller.forms import ClienteForm
from taller.models import Cliente


def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'taller/clientes/cliente_list.html', {'clientes': clientes})


def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'taller/clientes/cliente_detail.html', {'cliente': cliente})


@login_required
@permission_required('taller.add_cliente', raise_exception=True)
def cliente_create(request):
    form = ClienteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Cliente creado exitosamente.')
        return redirect('cliente_list')
    return render(request, 'taller/clientes/formulario.html', {'form': form})


@login_required
@permission_required('taller.change_cliente', raise_exception=True)
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Cliente actualizado exitosamente.')
        return redirect('cliente_list')
    return render(request, 'taller/clientes/formulario.html', {'form': form})


@login_required
@permission_required('taller.delete_cliente', raise_exception=True)
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('cliente_list')
    return render(request, 'taller/clientes/confirm_delete.html', {'objeto': cliente})
