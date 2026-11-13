from django.urls import path
from catalogo.views.libro_views import libro_list, create_libro, libro_update, libro_delete

urlpatterns = [
    path('libros/', libro_list, name='libro_list'),
    path('libros/nuevo/', create_libro, name='create_libro'),   
    path('libros/<int:pk>/editar/', libro_update, name='update_libro'),
    path('libros/<int:pk>/eliminar/', libro_delete, name='delete_libro'),
]