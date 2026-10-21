from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("aboutme", views.aboutme, name="aboutme"),
    path("saludo/<str:nombre>/", views.greeting, name="greeting"),
    path("destinatario/<str:titulo>/<str:nombre>/<str:cargo>/", views.destination, name="destination"),
    path("base-triangulo/<int:base>/<int:altura>/", views.base_triangulo, name="base-triangulo"),
    path("my-first-template/", views.my_first_template, name="my-first-template"),
]