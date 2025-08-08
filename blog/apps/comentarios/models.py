from django.db import models
from django.contrib.auth.models import User
from apps.articulos.models import Articulo

# Create your models here.
class Comentario(models.Model):

    #ATRIBUTOS del COMENTARIO
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=250)
    creado = models.DateTimeField(auto_now_add=True)    
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contenido

class LikeComentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='likes')
    likeado_en = models.DateTimeField(auto_now_add = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'comentario'], name='unique_like_comentario')
        ]

    
    def __str__(self):
        contador = self.comentario.likes.count()
        return f"El comentario: {self.comentario.contenido} tiene: {contador} likes"