from django.db import models
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
    #categoria autor likes

    def __str__(self):
        return self.titulo