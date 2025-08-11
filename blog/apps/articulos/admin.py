from django.contrib import admin
from .models import Articulo, LikeArticulo

# Register your models here.
admin.site.register(Articulo)
admin.site.register(LikeArticulo)