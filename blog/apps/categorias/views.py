from django.shortcuts import render, HttpResponseRedirect
from .models import Categoria 
from django.contrib.auth.decorators import login_required
from .forms import CategoriaForm
from django.urls import reverse_lazy 

# Create your views here.
@login_required
def Crear_Categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return HttpResponseRedirect(reverse_lazy('path_index'))
    else:
        form = CategoriaForm()
    return render(request, 'Categorias/crear_categoria.html', {'form': form})   