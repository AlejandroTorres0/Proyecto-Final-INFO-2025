from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, unique = True, blank = False)
    imagen = models.ImageField(upload_to = 'usuarios')
#   admin = models.BooleanField()

    def __str__(self):
        return self.nombreusuario