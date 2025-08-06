from django.urls import path
from django.contrib.auth import views as auth
from . import views

app_name = 'usuarios'

urlpatterns = [

    path('Login/', auth.LoginView.as_view(template_name='usuarios/login.html'),name = 'path_login'),
    path('Logout/', auth.LogoutView.as_view(),name = 'path_logout'),

    path('Registro/',views.RegistroUsuario.as_view(), name = 'path_registro'),

]