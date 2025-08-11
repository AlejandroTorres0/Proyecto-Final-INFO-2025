from django.contrib import admin
from .models import Comentario, LikeComentario

# Register your models here.
admin.site.register(Comentario)
admin.site.register(LikeComentario)