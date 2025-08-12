from django.db import models
from django.contrib.auth.models import User
from apps.categorias.models import Categoria
from django.utils.text import slugify

# Create your models here.
class Articulo(models.Model):
    
    #ATRIBUTOS del ARTICULO
    creado = models.DateTimeField(auto_now_add=True)    
    modificado = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    imagen = models.ImageField(upload_to = 'articulos')
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)   
    resumen = models.CharField(max_length=350, null = True)

    def __str__(self):
        return self.titulo
    
    def misComentarios(self):
        return self.comentario_set.all()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

class LikeArticulo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='likes')
    likeado_en = models.DateTimeField(auto_now_add = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'articulo'], name='unique_like_articulo')
        ]
    
    def __str__(self):
        contador = self.articulo.likes.count()
        return f"El comentario: {self.articulo.titulo} tiene: {contador} likes"