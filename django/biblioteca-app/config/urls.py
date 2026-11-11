
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('categorias/', include('catalogo.urls.categoria_urls')),
]
=======
    path('', include('catalogo.urls.home_urls')),
    path('admin/', admin.site.urls),
    path('catalogo/', include('catalogo.urls.categoria_urls')),
    path('catalogo/', include('catalogo.urls.libro_urls')),
]
 
>>>>>>> 427a68f (feat(2026-11-10): crud de categorias y Libros en biblioteca app)
