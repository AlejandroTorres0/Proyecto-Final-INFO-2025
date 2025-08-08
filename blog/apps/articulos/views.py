from django.shortcuts import render, redirect
from django.core.paginator import Paginator 
from .forms import ArticuloForm
from .models import Articulo, Categoria
from .utils import ordenar_articulos, paginar_articulos, obtener_siguiente_anterior

# Create your views here.

def Listar_Articulos(request):
    # Aquí iría la lógica para listar los artículos

    valor_a_ordenar = request.GET.get('orden', None)
    articulos = Articulo.objects.all()
    articulos_ordenados = ordenar_articulos(articulos, valor_a_ordenar)

    articulos_paginados = paginar_articulos(request, articulos_ordenados, 1, 6)[0]
    rango_paginas = paginar_articulos(request, articulos_ordenados, 1, 6)[1]

    categorias_bd = Categoria.objects.all()

    context = {
        'categorias':categorias_bd, 
        'articulos_p': articulos_paginados, 
        'rango_paginas': rango_paginas
    }

    return render(request, 'articulos/blog.html', context)

def Filtrar_Categoria(request, pk):
    categoria_filtrada = Categoria.objects.get(pk = pk)

    articulos_filtrados = Articulo.objects.filter(categoria = categoria_filtrada)
    
    valor_a_ordenar = request.GET.get('orden', None)
    articulos_ordenados = ordenar_articulos(articulos_filtrados, valor_a_ordenar)

    articulos_paginados = paginar_articulos(request, articulos_ordenados, 1, 6)[0]
    rango_paginas = paginar_articulos(request, articulos_ordenados, 1, 6)[1]

    categorias_bd = Categoria.objects.all()

    context = {
            'categorias': categorias_bd,
            'articulos_p': articulos_paginados, 
            'id_categoria': categoria_filtrada.id,
            'nombre_categoria': categoria_filtrada.nombre,
            'rango_paginas': rango_paginas
    }

    return render(request, 'articulos/blog.html', context)

def Detalle_Articulo(request, pk):
    articulo = Articulo.objects.get(pk = pk)

    articulo_anterior, articulo_siguiente = obtener_siguiente_anterior(articulo)
                                              
    categorias_bd = Categoria.objects.all()

    #Lógica para mostrar los likes ya likeados
    comentarios = articulo.misComentarios()

    usuario = request.user 
    if usuario.is_authenticated: 
        for comentario in comentarios:
            comentario.ya_likeado = comentario.likes.filter(usuario=usuario).exists()

    context = {
            'comentarios': comentarios,
            'categorias': categorias_bd,
            'articulo': articulo,
            'articulo_anterior':  articulo_anterior,
            'articulo_siguiente': articulo_siguiente
    }

    return render(request, 'articulos/Detalles_Blog.html', context)

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