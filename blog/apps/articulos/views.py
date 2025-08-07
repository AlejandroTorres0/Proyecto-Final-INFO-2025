from django.shortcuts import render, redirect
from .models import Articulo
from .models import Categoria
from django.core.paginator import Paginator 
from .forms import ArticuloForm

# Create your views here.

def Listar_Articulos(request):
    # Aquí iría la lógica para listar los artículos
    p = Paginator(Articulo.objects.all(), 1) #Cuantos articulos se van a mostrar por página
    page = request.GET.get('page')
    articulos_paginados = p.get_page(page)

    categorias_bd = Categoria.objects.all()

    total_paginas = p.num_pages
    pagina_actual = articulos_paginados.number

    tamano_bloque = 6
    principio_bloque = ((pagina_actual - 1) // tamano_bloque) * tamano_bloque + 1
    final_bloque = min(principio_bloque + tamano_bloque, total_paginas + 1)

    rango_paginas = range(principio_bloque, final_bloque)

    context = {
        'categorias':categorias_bd, 
        'articulos_p': articulos_paginados, 
        'rango_paginas': rango_paginas
    }

    return render(request, 'articulos/blog.html', context)


def Crear_Articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.usuario = request.user  # Asigna el usuario actual
            articulo.save()
            return redirect('articulos/blog.html')  # Cambia esto por tu URL
    else:
        form = ArticuloForm()
    return render(request, 'articulos/crear_articulo.html', {'form': form})