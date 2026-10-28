# tasks/admin.py
from django.contrib import admin
from .models import Project, Carpinteria, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
        list_display ("title", "project", "status", "due date")
        list_filter ("status", "project")
search_fields ("title", "description")


@admin.register(Nave)

class ProjectAdmin(admin.ModelAdmin):
    list_display ("nombre",
    "tipo_nave",
    "created_at")    
    search_fields("nombre", "tipo_nave")

@admin.register(Carpinteria)
class ProyectAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "edad", "profesion")
    search_fields = ("nombre", "apellido")