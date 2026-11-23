from django.contrib import admin

from taller.models import Categoria, Cliente, Mueble, Pedido


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'telefono', 'email')
    search_fields = ('nombre', 'apellido', 'telefono')


@admin.register(Mueble)
class MuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'mueble', 'cantidad', 'estado', 'fecha_pedido')
    list_filter = ('estado', 'fecha_pedido')