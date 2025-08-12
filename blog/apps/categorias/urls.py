from django.urls import path
from . import views 

app_name = "categorias"

urlpatterns = [
    path('CrearCategoria', views.Crear_Categoria, name="path_crear_categoria"),
    path('EditarCategoria/<int:pk>', views.EditarCategoria.as_view(), name="path_editar_categoria"),
    path('EliminarCategoria/<int:pk>', views.EliminarCategoria.as_view(), name="path_eliminar_categoria")
]