from django.contrib import admin
from django.contrib.auth.models import User
from .models import PerfilUsuario

# Register your models here.
admin.site.register(PerfilUsuario)

class PerfilEnLinea(admin.StackedInline):
    model = PerfilUsuario

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [PerfilEnLinea]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)