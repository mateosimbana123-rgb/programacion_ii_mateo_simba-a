from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from taller.forms import RegistroForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            consultores, created = Group.objects.get_or_create(name='consultores')
            user.groups.add(consultores)
            messages.success(request, 'Registro completado exitosamente.')
            login(request, user)
            return redirect('mueble_list')
    else:
        form = RegistroForm()
    return render(request, 'taller/authentication/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user is not None:
            login(request, user)
            return redirect('mueble_list')
        messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'taller/authentication/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('mueble_list')
    return render(request, 'taller/authentication/logout.html')
