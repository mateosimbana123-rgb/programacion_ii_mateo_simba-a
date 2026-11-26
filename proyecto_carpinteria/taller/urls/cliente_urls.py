from django.urls import path

from taller.views import (
    cliente_list,
    cliente_detail,
    cliente_create,
    cliente_update,
    cliente_delete,
)

urlpatterns = [
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/<int:pk>/', cliente_detail, name='cliente_detail'),
    path('clientes/nuevo/', cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', cliente_delete, name='cliente_delete'),
]
