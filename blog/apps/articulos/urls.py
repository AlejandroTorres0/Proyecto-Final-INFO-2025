from django.urls import path
from . import views

#Nombre de la app
app_name = "articulos"

urlpatterns = [
    #1* Parametro, que es la url
    #2* Parametro, que es la vista
    #3* Parametro, que es el nombre del path

    path('Listar', views.Listar_Articulos, name = 'path_listar_articulos'),
]
