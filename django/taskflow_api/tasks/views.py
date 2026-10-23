from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>

    """)

def home(request):
    return HttpResponse("Bienvenido a TaskFlow")

def register(request):
    return HttpResponse("Registro de usuarios")

def login(request):
    return HttpResponse("Login de Usuarios en aplicacion")

def aboutme(request):
    return HttpResponse("Acerca de mí")

def greeting(request, nombre):
    return HttpResponse(f"Hola {nombre}, bienvenido a taskflow")

def destination(request, titulo, nombre, cargo):
    return HttpResponse(f"Bienvenido: {titulo} {nombre}, su cargo es: {cargo}")

def base_triangulo(request, base, altura):
    area = (int(base) * int(altura)) / 2
    return HttpResponse(f"El área del triángulo es: {area}")

def my_first_template(request):
    return HttpResponse("Mi primera plantilla")

def leads_like(request):
    contexto={
        "titulo": "Programador",
        "nombre": "Mateo",
        "apellido": "Simbaña",
    }
    return render(request, "leads/leads-like.html",contexto)