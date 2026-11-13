from django.urls import path
from catalogo.views.Autor_views import (Autor_delete, Autor_list, Autor_create)   

urlpatterns = [
    path('Autors/', Autor_list, name='Autor_list'),
    path('catalogo/nueva/', Autor_create, name='Autor_create'),
    path('Autors/<int:pk>/eliminar/', Autor_delete, name='Autor_delete'),
    path('Autors/<int:pk>/editar/', Autor_create, name='Autor_update'),
]