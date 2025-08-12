from django.shortcuts import render, HttpResponseRedirect
from .models import Categoria 
from django.contrib.auth.decorators import login_required
from .forms import CategoriaForm, FormularioEditarCategoria
from django.urls import reverse_lazy 
from apps.articulos.utils import obtener_n_populares
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def Crear_Categoria(request):
    #Base
    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]

    if request.method == 'POST' and request.user.is_staff:
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return HttpResponseRedirect(reverse_lazy('path_index'))
    else:
        form = CategoriaForm()
    
    context = {
        'form': form, 
        'articulos_populares': populares,
        'articulos_populares_footer': articulos_populares_footer
    }        
    return render(request, 'Categorias/crear_categoria.html', context)   

class EditarCategoria(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Categoria
    form_class = FormularioEditarCategoria
    template_name = 'Categorias/editar_categoria.html'
        
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    
    def get_success_url(self):
        return reverse_lazy('articulos:path_listar_articulos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        populares = obtener_n_populares(5)
        articulos_populares_footer = populares[:3]

        context['articulos_populares'] = populares 
        context['articulos_populares_footer'] = articulos_populares_footer
        return context 

class EliminarCategoria(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Categoria
    template_name = 'Categorias/eliminar_categoria.html'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    
    def get_success_url(self):
        return reverse_lazy('articulos:path_listar_articulos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        populares = obtener_n_populares(5)
        articulos_populares_footer = populares[:3]

        context['articulos_populares'] = populares 
        context['articulos_populares_footer'] = articulos_populares_footer
        return context