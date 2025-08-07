from django.urls import path
from . import views 

app_name = 'Categorias'

urlpatterns = [
    path('categoria', views.categorias, name='path_categorias') 
]