from django.urls import path
from taller.views import (
    mueble_list, mueble_create, mueble_update, mueble_delete,
    categoria_list, categoria_create, categoria_update, categoria_delete,
    cliente_list, cliente_create, cliente_update, cliente_delete,
    pedido_list, pedido_create, pedido_update, pedido_delete,
)

urlpatterns = [
    path('', mueble_list, name='mueble_list'),
    path('crear/', mueble_create, name='mueble_create'),
    path('<int:pk>/editar/', mueble_update, name='mueble_update'),
    path('<int:pk>/eliminar/', mueble_delete, name='mueble_delete'),
    path('categorias/', categoria_list, name='categoria_list'),
    path('categorias/nueva/', categoria_create, name='categoria_create'),
    path('categorias/<int:pk>/editar/', categoria_update, name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', categoria_delete, name='categoria_delete'),
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/nuevo/', cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', cliente_delete, name='cliente_delete'),
    path('pedidos/', pedido_list, name='pedido_list'),
    path('pedidos/nuevo/', pedido_create, name='pedido_create'),
    path('pedidos/<int:pk>/editar/', pedido_update, name='pedido_update'),
    path('pedidos/<int:pk>/eliminar/', pedido_delete, name='pedido_delete'),
]