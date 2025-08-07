from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #1* Parametro, que es la url
    #2* Parametro, que es la vista
    #3* Parametro, que es el nombre del path
    path('', views.Index, name = "path_index"),
    path('Sobre_nosotros/', views.sobre_nosotros, name = "path_sobre_nosotros"),
    path('Novedades/', views.novedades, name = "path_novedades"),
    path('Contactanos/', views.contactanos, name = "path_contactanos"),
    
    #Incluir las apps
    path('Articulos/', include('apps.articulos.urls')),
    path('Usuarios/', include('apps.usuarios.urls')),
    path('Categorias/', include('apps.categorias.urls')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

