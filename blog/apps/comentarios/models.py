from django.db import models
from usuarios.models import Usuario
from apps.articulos.models import Articulo

# Create your models here.
class Comentario(models.Model):

    #ATRIBUTOS del COMENTARIO
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=250)
    likes = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)    
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.texto #podria ser nombre de usuario y fecha nomas