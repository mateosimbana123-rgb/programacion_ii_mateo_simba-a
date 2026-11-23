from django.urls import path
from catalogo.views.autor_views import (
    Autor_create,
    Autor_delete,
    Autor_list,
    Autor_update,
)

urlpatterns = [
    path('autores/', Autor_list, name='autor_list'),
    path('autores/nuevo/', Autor_create, name='create_autor'),
    path('autores/<int:pk>/editar/', Autor_update, name='update_autor'),
    path('autores/<int:pk>/eliminar/', Autor_delete, name='delete_autor'),
]
