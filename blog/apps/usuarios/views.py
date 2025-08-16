from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioRegistroUsuario, CambiarContrasenaForm, EditarPerfilForm, EditarUsuarioForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login 

# Create your views here.
class CambiarContrasenaViewPersonalizada(PasswordChangeView):
    form_class = CambiarContrasenaForm
    template_name='usuarios/cambiar_contrasena.html'
    success_url = reverse_lazy('usuarios:path_cambiar_contrasena_exito')

@login_required 
def CambiarContrasenaExito(request):
    return render(request, 'usuarios/cambio_contrasena_exito.html')

@login_required
def VerPerfil(request):
    usuario = User.objects.get(id = request.user.id)
    perfil = usuario.perfil

    if request.user.is_authenticated: 
        context = {
            'usuario': usuario, 
            'perfil': perfil,
        }
        
    return render(request, 'usuarios/perfil.html', context)
    
@login_required
def EditarPerfil(request):
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
        }

        return render(request, 'usuarios/editar_perfil.html', context)
    else: 
        messages.succes(request, 'Debes estar logeado para acceder a esa página.')
        return redirect('path_index')

class RegistroUsuario(CreateView):
    template_name = 'usuarios/registro.html'
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy('usuarios:path_login')