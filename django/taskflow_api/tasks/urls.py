from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.project_list, name="project-list"),
    path("projects/new/", views.project_create, name="project-create"),
    path("projects/<int:project_id>/edit/", views.project_update, name="project-update"),
    path("projects/<int:project_id>/delete/", views.project_delete, name="project-delete"),
    path("tasks/new/", views.task_create, name="task-create"),
    path("tasks/<int:task_id>/edit/", views.task_update, name="task-update"),
    path("tasks/<int:task_id>/delete/", views.task_delete, name="task-delete"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("aboutme/", views.aboutme, name="aboutme"),
    path("saludo/<str:nombre>/", views.greeting, name="greeting"),
    path("destinatario/<str:titulo>/<str:nombre>/<str:cargo>/", views.destination, name="destination"),
    path("base-triangulo/<int:base>/<int:altura>/", views.base_triangulo, name="base-triangulo"),
    path("my-first-template/", views.my_first_template, name="my-first-template"),
    path("leads-like/", views.leads_like, name="leads-like"),
]