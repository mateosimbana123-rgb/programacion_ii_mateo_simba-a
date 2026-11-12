from django.contrib.auth.views import LoginView, logoutView

class BibliotecaLoginView(LoginView):
    template_name = 'catalogo/login.html'
    redirect_authenticated_user = True

class BibliotecaLogoutView(logoutView):
    template_name = 'catalogo/logout.html'
    next_page = 'login'