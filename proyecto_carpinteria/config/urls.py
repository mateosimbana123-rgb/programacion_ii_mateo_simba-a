from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taller.urls.mueble_urls')),
    path('', include('taller.urls.categoria_urls')),
    path('', include('taller.urls.cliente_urls')),
    path('', include('taller.urls.pedido_urls')),
    path('', include('taller.urls.auth_urls')),
]