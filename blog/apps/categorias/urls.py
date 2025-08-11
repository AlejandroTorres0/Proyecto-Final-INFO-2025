from django.urls import path
from . import views 

app_name = "categorias"

urlpatterns = [
    path('CrearCategoria', views.Crear_Categoria, name="path_crear_categoria") 
]