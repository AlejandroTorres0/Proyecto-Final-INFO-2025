from django.urls import path
from django.contrib.auth import views as auth
from . import views

app_name = 'usuarios'

urlpatterns = [

    path('Login/',  auth.LoginView.as_view(template_name='usuarios/login.html'),name = 'path_login'),
    path('Logout/', auth.LogoutView.as_view(template_name='index.html'), name = 'path_logout'),

    path('Registro/',views.RegistroUsuario.as_view(), name = 'path_registro'),

    path('CambiarContrasena/', views.CambiarContrasenaViewPersonalizada.as_view(), name='path_cambiar_contrasena'),
    path('CambiarContrasenaExito/', views.CambiarContrasenaExito, name='path_cambiar_contrasena_exito'),

    path('EditarPerfil/', views.EditarPerfil, name='path_editar_perfil'),
    path('Perfil/', views.VerPerfil, name='path_perfil')
]