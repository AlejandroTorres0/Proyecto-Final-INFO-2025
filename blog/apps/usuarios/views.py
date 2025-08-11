from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioRegistroUsuario
from django.contrib.auth.views import LoginView
from apps.articulos.utils import obtener_n_populares

# Create your views here.
class RegistroUsuario(CreateView):
    template_name = 'usuarios/registro.html'
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy('usuarios:path_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        populares = obtener_n_populares(5)
        articulos_populares_footer = populares[:3]

        context['articulos_populares'] = populares 
        context['articulos_populares_footer'] = articulos_populares_footer
        return context


class LoginViewPersonalizada(LoginView):
    template_name = "usuarios/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        populares = obtener_n_populares(5)
        articulos_populares_footer = populares[:3]

        context['articulos_populares'] = populares 
        context['articulos_populares_footer'] = articulos_populares_footer
        return context