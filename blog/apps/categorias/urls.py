from django.urls import path
from . import views 

app_name = "categorias"

urlpatterns = [
    path('Categorias', views.categorias, name="path_ver_categorias") 
]