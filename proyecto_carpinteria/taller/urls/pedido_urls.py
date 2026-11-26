from django.urls import path

from taller.views import (
    pedido_list,
    pedido_detail,
    pedido_create,
    pedido_update,
    pedido_delete,
)

urlpatterns = [
    path('pedidos/', pedido_list, name='pedido_list'),
    path('pedidos/<int:pk>/', pedido_detail, name='pedido_detail'),
    path('pedidos/nuevo/', pedido_create, name='pedido_create'),
    path('pedidos/<int:pk>/editar/', pedido_update, name='pedido_update'),
    path('pedidos/<int:pk>/eliminar/', pedido_delete, name='pedido_delete'),
]
