from django.urls import path

from taller.views import login_view, logout_view, registro

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
