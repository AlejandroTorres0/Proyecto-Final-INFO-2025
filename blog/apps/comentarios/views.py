from django.shortcuts import render, HttpResponseRedirect
from .models import Comentario, Articulo, LikeComentario
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import FormularioEditarComentario
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def Comentar(request, pk):
    if request.method == 'POST':
        articulo = Articulo.objects.get(pk = pk)
        usuario = request.user
        com = request.POST.get('comentario', None)
        Comentario.objects.create(contenido = com, articulo = articulo,  usuario = usuario)

    return HttpResponseRedirect(reverse_lazy('articulos:path_articulo_detalle', kwargs = {'pk': pk} ))


class EditarComentario(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Comentario
    form_class = FormularioEditarComentario
    template_name = 'comentarios/editar_comentario.html'

    def test_func(self):
        comentario = self.get_object()
        return self.request.user == comentario.usuario or self.request.user.is_staff
    
    def handle_no_permission(self):
        return HttpResponseForbidden("No tienes permiso para editar este comentario.")

    def get_success_url(self):
        return reverse_lazy('articulos:path_articulo_detalle', kwargs={'pk':self.object.articulo.pk})

class EliminarComentario(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Comentario
    template_name = 'comentarios/eliminar_comentario.html'

    def test_func(self):
        comentario = self.get_object()
        return self.request.user == comentario.usuario or self.request.user.is_staff
    
    def handle_no_permission(self):
        return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")
    
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