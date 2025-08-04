from django.db import models
from django.contrib.auth.models import User
from categorias.models import Categoria

# Create your models here.
class Articulo(models.Model):
    
    #ATRIBUTOS del ARTICULO
    creado = models.DateTimeField(auto_now_add=True)    
    modificado = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    imagen = models.ImageField(upload_to = 'articulos')
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)   

    def __str__(self):
        return self.titulo
    
class LikeArticulo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='likes')
    likeado_en = models.DateTimeField(auto_now_add = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'articulo'], name='unique_like_articulo')
        ]