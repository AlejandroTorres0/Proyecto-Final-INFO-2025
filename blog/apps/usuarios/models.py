from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    avatar = models.ImageField(upload_to = 'usuario/', default='usuario/default.png')


    def __str__(self):
        return self.usuario.username
    

def crearPerfilUsuario(sender, instance, created, **kwargs):
    if created: 
        perfil_usuario = PerfilUsuario(usuario=instance)
        perfil_usuario.save()

post_save.connect(crearPerfilUsuario, sender = User)