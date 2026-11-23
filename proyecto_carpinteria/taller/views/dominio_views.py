from django.shortcuts import get_object_or_404, redirect, render

from taller.forms import CategoriaForm, ClienteForm, PedidoForm
from taller.models import Categoria, Cliente, Pedido


def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'taller/categoria_list.html', {'categorias': categorias})


def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('categoria_list')
    return render(request, 'taller/formulario.html', {'form': form})


def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('categoria_list')
    return render(request, 'taller/formulario.html', {'form': form})


def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'taller/confirm_delete.html', {'objeto': categoria})


def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'taller/cliente_list.html', {'clientes': clientes})


def cliente_create(request):
    form = ClienteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'taller/formulario.html', {'form': form})


def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'taller/formulario.html', {'form': form})


def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'taller/confirm_delete.html', {'objeto': cliente})


def pedido_list(request):
    pedidos = Pedido.objects.select_related('cliente', 'mueble').all()
    return render(request, 'taller/pedido_list.html', {'pedidos': pedidos})


def pedido_create(request):
    form = PedidoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pedido_list')
    return render(request, 'taller/formulario.html', {'form': form})


def pedido_update(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    form = PedidoForm(request.POST or None, instance=pedido)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pedido_list')
    return render(request, 'taller/formulario.html', {'form': form})


def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedido_list')
    return render(request, 'taller/confirm_delete.html', {'objeto': pedido})
