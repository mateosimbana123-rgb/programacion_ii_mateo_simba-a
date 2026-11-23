
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('catalogo.urls.home_urls')),
    path('', include('catalogo.urls.autentication_urls')),
    path('', include('catalogo.urls.categoria_urls')),
    path('', include('catalogo.urls.libro_urls')),
    path('', include('catalogo.urls.autor_urls')),
]