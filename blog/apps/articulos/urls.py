from django.urls import path
from . import views

#Nombre de la app
app_name = "articulos"

urlpatterns = [
    #1* Parametro, que es la url
    #2* Parametro, que es la vista
    #3* Parametro, que es el nombre del path

    path('Listar', views.Listar_Articulos, name = 'path_listar_articulos'),
    path('Filtrado/<int:pk>', views.Filtrar_Categoria, name='path_filtrar_categoria'),
    path('Detalle/<int:pk>', views.Detalle_Articulo, name="path_articulo_detalle")
    path('Crear', views.Crear_Articulo, name = 'path_crear_articulo'),
]
