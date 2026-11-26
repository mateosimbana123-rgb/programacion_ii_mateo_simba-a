from django.urls import path

from taller.views import mueble_list, mueble_detail, mueble_create, mueble_update, mueble_delete

urlpatterns = [
    path('', mueble_list, name='mueble_list'),
    path('muebles/crear/', mueble_create, name='mueble_create'),
    path('muebles/<int:pk>/', mueble_detail, name='mueble_detail'),
    path('muebles/<int:pk>/editar/', mueble_update, name='mueble_update'),
    path('muebles/<int:pk>/eliminar/', mueble_delete, name='mueble_delete'),
]