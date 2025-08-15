from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioRegistroUsuario, CambiarContrasenaForm, EditarPerfilForm, EditarUsuarioForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.models import User
from apps.articulos.utils import obtener_n_populares
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
class CambiarContrasenaViewPersonalizada(PasswordChangeView):
    form_class = CambiarContrasenaForm
    template_name='usuarios/cambiar_contrasena.html'
    success_url = reverse_lazy('usuarios:path_cambiar_contrasena_exito')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        populares = obtener_n_populares(5)
        articulos_populares_footer = populares[:3]

        context['articulos_populares'] = populares
        context['articulos_populares_footer'] = articulos_populares_footer
        return context

def CambiarContrasenaExito(request):
    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]
    context = {
        'articulos_populares': populares,
        'articulos_populares_footer': articulos_populares_footer
    }
    return render(request, 'usuarios/cambio_contrasena_exito.html', context)

@login_required
def VerPerfil(request):
    usuario = User.objects.get(id = request.user.id)
    perfil = usuario.perfil

    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]


    context = {
            'usuario': usuario,
            'perfil': perfil,
            'articulos_populares': populares,
            'articulos_populares_footer': articulos_populares_footer
    }

    return render(request, 'usuarios/perfil.html', context)

@login_required
def EditarPerfil(request):
    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]

    usuario = User.objects.get(id = request.user.id)
    perfil = usuario.perfil

    if request.user.is_authenticated:
        perfil_form = EditarPerfilForm(request.POST, request.FILES, instance=perfil)
        user_form = EditarUsuarioForm(request.POST or None, instance=usuario)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()

            login(request, usuario)
            messages.success(request, 'Su perfil fue editado correctamente!!')
            return redirect('path_index')
        context = {
            'user_form': user_form,
            'perfil_form': perfil_form,

            'articulos_populares': populares,
            'articulos_populares_footer': articulos_populares_footer
        }

        return render(request, 'usuarios/editar_perfil.html', context)
    else:
        messages.success(request, 'Debes estar logeado para acceder a esa página.')
        return redirect('path_index')

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