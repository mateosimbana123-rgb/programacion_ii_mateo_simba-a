from django.contrib import admin

# tasks/admin.py
from django.contrib import admin
from .models import Project, Carpinteria


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Carpinteria)
class ProyectAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "edad", "profesion")
    search_fields = ("nombre", "apellido")