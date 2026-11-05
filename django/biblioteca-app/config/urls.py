
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', include('catalogo.urls.categoria_urls')),
]
