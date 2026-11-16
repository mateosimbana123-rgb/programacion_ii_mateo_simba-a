from django.urls import path
from taller.views import mueble_list, mueble_create

urlpatterns = [
    path('', mueble_list, name='mueble_list'),
    path('crear/', mueble_create, name='mueble_create'),
]