from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def articulosRelacionados(self):
        return self.articulo_set.all()
        
    def __str__(self):
        return self.nombre

    class Meta: #Orden ascendente (a-z) por campo nombre
        verbose_name_plural = "Categorías"
        ordering = ['nombre']