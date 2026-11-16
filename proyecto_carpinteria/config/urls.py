from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('muebles/', include('taller.urls.mueble_urls')),
]