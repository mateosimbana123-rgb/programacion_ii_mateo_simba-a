from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from taller.forms import PedidoForm
from taller.models import Pedido


def pedido_list(request):
    pedidos = Pedido.objects.select_related('cliente', 'mueble').all()
    return render(request, 'taller/pedidos/pedido_list.html', {'pedidos': pedidos})


def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido.objects.select_related('cliente', 'mueble'), pk=pk)
    return render(request, 'taller/pedidos/pedido_detail.html', {'pedido': pedido})


@login_required
@permission_required('taller.add_pedido', raise_exception=True)
def pedido_create(request):
    form = PedidoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        pedido = form.save(commit=False)
        pedido.creado_por = request.user
        pedido.save()
        messages.success(request, 'Pedido creado exitosamente.')
        return redirect('pedido_list')
    return render(request, 'taller/pedidos/formulario.html', {'form': form})


@login_required
@permission_required('taller.change_pedido', raise_exception=True)
def pedido_update(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if not request.user.groups.filter(name='administradores').exists() and pedido.creado_por != request.user:
        raise PermissionDenied
    form = PedidoForm(request.POST or None, instance=pedido)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Pedido actualizado exitosamente.')
        return redirect('pedido_list')
    return render(request, 'taller/pedidos/formulario.html', {'form': form})


@login_required
@permission_required('taller.delete_pedido', raise_exception=True)
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if not request.user.groups.filter(name='administradores').exists() and pedido.creado_por != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado exitosamente.')
        return redirect('pedido_list')
    return render(request, 'taller/pedidos/confirm_delete.html', {'objeto': pedido})
