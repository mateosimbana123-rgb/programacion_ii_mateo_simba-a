from django.urls import path
from catalogo.views.libros_views import libro_list, create_libro

urlspatterns = [
    path('', home_view, name='home')
]