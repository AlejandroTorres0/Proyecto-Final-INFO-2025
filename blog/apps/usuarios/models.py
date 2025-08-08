from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    avatar = models.ImageField(upload_to = 'usuario/')


    def __str__(self):
        return self.usuario.username