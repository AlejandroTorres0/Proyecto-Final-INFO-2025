from django.shortcuts import render, HttpResponseRedirect
from .models import Categoria 
from django.contrib.auth.decorators import login_required
from .forms import CategoriaForm
from django.urls import reverse_lazy 
from apps.articulos.utils import obtener_n_populares

# Create your views here.
@login_required
def Crear_Categoria(request):
    #Base
    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]

    if request.method == 'POST':
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