from django.shortcuts import render, HttpResponseRedirect
from .models import Comentario, Articulo, LikeComentario
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import FormularioEditarComentario
# Create your views here.
@login_required
def Comentar(request, pk):
    articulo = Articulo.objects.get(pk = pk)
    usuario = request.user
    com = request.POST.get('comentario', None)
    Comentario.objects.create(contenido = com, articulo = articulo,  usuario = usuario)

    return HttpResponseRedirect(reverse_lazy('articulos:path_articulo_detalle', kwargs = {'pk': pk} ))


class EditarComentario(UpdateView, LoginRequiredMixin): 
    model = Comentario
    form_class = FormularioEditarComentario
    template_name = 'Comentarios/editar_comentario.html'

    #Verificacion de que el comentario es del usuario que hace la request      

    def get_success_url(self):
        return reverse_lazy('articulos:path_articulo_detalle', kwargs={'pk':self.object.articulo.pk})

class EliminarComentario(DeleteView, LoginRequiredMixin): 
    model = Comentario
    template_name = 'comentarios/eliminar_comentario.html'

    #Verificacion de que el comentario es del usuario que hace la request      

    def get_success_url(self):
        return reverse_lazy('articulos:path_articulo_detalle', kwargs={'pk':self.object.articulo.pk})

@login_required
def LikearComentario(request, pk_comentario, pk_articulo):
    usuario = request.user
    comentario = Comentario.objects.get(pk = pk_comentario)
    LikeComentario.objects.create(comentario = comentario, usuario = usuario)

    return HttpResponseRedirect(reverse_lazy('articulos:path_articulo_detalle', kwargs = {'pk': pk_articulo} ))

@login_required
def DeslikearComentario(request, pk_comentario, pk_articulo):
    usuario = request.user
    comentario = Comentario.objects.get(pk = pk_comentario)
    like = LikeComentario.objects.filter(comentario = comentario, usuario = usuario)
    like.delete()

    return HttpResponseRedirect(reverse_lazy('articulos:path_articulo_detalle', kwargs = {'pk': pk_articulo} ))