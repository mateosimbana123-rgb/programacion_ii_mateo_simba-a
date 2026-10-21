from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("Hola, TaskFlow")

def register(request):
    """Registro de usuarios"""
    return HttpResponse("Registro de Usuarios en Lista")

def login(request):
    """Login de usuarios"""
    return HttpResponse("Login de usuarios en aplicacion")

def greeting (request, nombre):
    """Regisytro de usuarios"""
    return HttpRespose(
    f"Hola{nombre}, bienvenido a taskflow")

def destination(request, titulo, nombre, cargo):
    """Regisytro de usuarios"""
    return HttpRespose(
        f"Bienvenido:{titulo}{nombre}, tu cargo es:{cargo}"

def destination(request, base, altura):
    """Registro de usuarios"""
    return HttpRespose(
        f"El area del triangulo es:{(base*altura)/2}")