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
    #Incluir las apps
    path('Articulos/', include('apps.articulos.urls')),
    path('Usuarios/', include('apps.usuarios.urls')),
    #path('login/', include ('login.urls'))
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

