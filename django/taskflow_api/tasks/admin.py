# tasks/admin.py
from django.contrib import admin
from .models import (
    Actividad,
    Alumno,
    Carpinteria,
    Comida,
    Estudiante,
    Mision,
    Nave,
    Participacion,
    Perfil,
    Project,
    Sensei,
    Task,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description")


@admin.register(Nave)
class NaveAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo_nave", "created_at")
    search_fields = ("nombre", "tipo_nave")


@admin.register(Carpinteria)
class CarpinteriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "edad", "profesion")
    search_fields = ("nombre", "apellido")


@admin.register(Comida)
class ComidaAdmin(admin.ModelAdmin):
    list_display = ("nombre_comida", "categoria", "created_at")
    search_fields = ("nombre_comida", "categoria")


@admin.register(Sensei)
class SenseiAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edad", "created_at")
    search_fields = ("nombre",)


@admin.register(Mision)
class MisionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "created_at")
    search_fields = ("titulo",)


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "sensei", "edad", "created_at")
    list_filter = ("sensei",)
    search_fields = ("nombre", "sensei__nombre")
    filter_horizontal = ("misiones",)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("alumno", "created_at")
    search_fields = ("alumno__nombre",)


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created_at")
    search_fields = ("nombre",)


class ParticipacionInline(admin.TabularInline):
    model = Participacion
    extra = 1


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ("titulo", "objetivo")
    search_fields = ("titulo", "objetivo")
    inlines = (ParticipacionInline,)


@admin.register(Participacion)
class ParticipacionAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "actividad", "rol", "created_at")
    list_filter = ("actividad", "rol")
    search_fields = ("estudiante__nombre", "actividad__titulo", "rol")
