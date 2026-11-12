from django.urls import path
from catalogo.views.libros_views import libro_list, create_libro


urlspatterns = [
    path('libros/', libro_list, name='libro_list'),
    path('libros/nuevo/', create_libro, name='create_libro'),   
    path('libros/<int:pk>/editar/', update_libro, name='update_libro'),
    path('libros/<int:pk>/eliminar/', delete_libro, name='delete_libro'),
]