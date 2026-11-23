from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_POST

from .forms import ProjectForm, TaskForm
from .models import Project, Task


def home(request):
    projects = Project.objects.prefetch_related("tasks").order_by("-created_at")
    return render(
        request,
        "task/home.html",
        {
            "titulo": "TaskFlow",
            "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
            "projects": projects,
        },
    )


def project_list(request):
    projects = Project.objects.prefetch_related("tasks").order_by("-created_at")
    return render(request, "projects/projects.html", {"projects": projects})


@require_http_methods(["GET", "POST"])
def project_create(request):
    data = request.POST if request.method == "POST" else None
    form = ProjectForm(data)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks:project-list")
    return render(
        request,
        "projects/project_form.html",
        {"form": form, "modo": "crear"},
    )


@require_http_methods(["GET", "POST"])
def project_update(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    data = request.POST if request.method == "POST" else None
    form = ProjectForm(data, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks:project-list")
    return render(
        request,
        "projects/project_form.html",
        {"form": form, "modo": "editar"},
    )


@require_http_methods(["GET", "POST"])
@require_POST
def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect("tasks:project-list")


@require_http_methods(["GET", "POST"])
def task_create(request):
    data = request.POST if request.method == "POST" else None
    form = TaskForm(data)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks:home")
    return render(request, "task/task_form.html", {"form": form, "modo": "crear"})


@require_http_methods(["GET", "POST"])
def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    data = request.POST if request.method == "POST" else None
    form = TaskForm(data, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks:home")
    return render(request, "task/task_form.html", {"form": form, "modo": "editar"})


@require_POST
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("tasks:home")


def register(request):
    return HttpResponse("Registro de usuarios")


def login(request):
    return HttpResponse("Login de Usuarios en aplicacion")


def aboutme(request):
    return HttpResponse("Acerca de mi")


def greeting(request, nombre):
    return HttpResponse(f"Hola {nombre}, bienvenido a taskflow")


def destination(request, titulo, nombre, cargo):
    return HttpResponse(f"Bienvenido: {titulo} {nombre}, su cargo es: {cargo}")


def base_triangulo(request, base, altura):
    area = (int(base) * int(altura)) / 2
    return HttpResponse(f"El area del triangulo es: {area}")


def my_first_template(request):
    return render(
        request,
        "task/my-first-template.html",
        {"titulo": "TaskFlow", "mensaje": "Organiza tus proyectos y tareas"},
    )


def leads_like(request):
    contexto={
        "titulo": "Programador",
        "nombre": "Mateo",
        "apellido": "Simbana",
    }
    return render(request, "leads/leads-like.html",contexto)