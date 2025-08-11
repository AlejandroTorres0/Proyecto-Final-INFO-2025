from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ArticuloForm, FormularioEditarArticulo
from .models import Articulo, Categoria, LikeArticulo
from .utils import ordenar_articulos, paginar_articulos, obtener_siguiente_anterior, ultimos_n_por_fecha, obtener_n_populares
from django.urls import reverse_lazy 
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.
def Listar_Articulos(request):
    # Aquí iría la lógica para listar los artículos
    #Base
    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]

    valor_a_ordenar = request.GET.get('orden', None)
    articulos = Articulo.objects.all()
    articulos_ordenados = ordenar_articulos(articulos, valor_a_ordenar)

    articulos_paginados = paginar_articulos(request, articulos_ordenados, 1, 6)[0]
    rango_paginas = paginar_articulos(request, articulos_ordenados, 1, 6)[1]

    ultimos_5 = ultimos_n_por_fecha(5)

    categorias_bd = Categoria.objects.all()



    context = {
        'articulos_populares': populares,
        'articulos_populares_footer': articulos_populares_footer, 

        'categorias':categorias_bd,
        'articulos_recientes': ultimos_5, 
        'articulos_p': articulos_paginados, 
        'rango_paginas': rango_paginas
    }

    return render(request, 'Articulos/blog.html', context)

def Filtrar_Categoria(request, pk):
    categoria_filtrada = Categoria.objects.get(pk = pk)

    articulos_filtrados = Articulo.objects.filter(categoria = categoria_filtrada)

    ultimos_5 = ultimos_n_por_fecha(5)

    valor_a_ordenar = request.GET.get('orden', None)
    articulos_ordenados = ordenar_articulos(articulos_filtrados, valor_a_ordenar)

    articulos_paginados = paginar_articulos(request, articulos_ordenados, 1, 6)[0]
    rango_paginas = paginar_articulos(request, articulos_ordenados, 1, 6)[1]

    categorias_bd = Categoria.objects.all()

    context = {
            'categorias': categorias_bd,
            'articulos_p': articulos_paginados,
            'articulos_recientes': ultimos_5, 
            'id_categoria': categoria_filtrada.id,
            'nombre_categoria': categoria_filtrada.nombre,
            'rango_paginas': rango_paginas
    }

    return render(request, 'Articulos/blog.html', context)

def Detalle_Articulo(request, pk):
    articulo = Articulo.objects.get(pk = pk)

    articulo_anterior, articulo_siguiente = obtener_siguiente_anterior(articulo)

    ultimos_5 = ultimos_n_por_fecha(5)

    categorias_bd = Categoria.objects.all()

    comentarios = articulo.misComentarios()

    usuario = request.user 
    if usuario.is_authenticated:
        #Lógica para mostrar los likes ya likeados
        for comentario in comentarios:
            comentario.ya_likeado = comentario.likes.filter(usuario=usuario).exists()
        
        articulo.ya_likeado = articulo.likes.filter(usuario=usuario).exists()

    context = {
            'comentarios': comentarios,
            'categorias': categorias_bd,
            'articulo': articulo,
            'articulos_recientes': ultimos_5,
            'articulo_anterior':  articulo_anterior,
            'articulo_siguiente': articulo_siguiente
    }

    return render(request, 'articulos/Detalles_Blog.html', context)

@login_required
def Crear_Articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.usuario = request.user  # Asigna el usuario actual
            articulo.save()
            return HttpResponseRedirect(reverse_lazy('articulos:path_listar_articulos'))
    else:
        form = ArticuloForm()
    return render(request, 'Articulos/crear_articulo.html', {'form': form})

class EditarArticulo(UpdateView, LoginRequiredMixin):
    model = Articulo
    form_class = FormularioEditarArticulo
    template_name = 'Articulos/editar_articulo.html'
    #Verificacion de que el comentario es del usuario que hace la request      

    def get_success_url(self):
        return reverse_lazy('articulos:path_articulo_detalle', kwargs={'pk':self.object.pk})

class EliminarArticulo(DeleteView, LoginRequiredMixin):
    model = Articulo
    template_name = 'Articulos/eliminar_articulo.html'
    #Verificacion de que el comentario es del usuario que hace la request      

    def get_success_url(self):
        return reverse_lazy('articulos:path_listar_articulos')

@login_required
def LikearArticulo(request, pk_articulo):
    usuario = request.user
    articulo = Articulo.objects.get(pk = pk_articulo)
    LikeArticulo.objects.create(articulo = articulo, usuario = usuario)

    return HttpResponseRedirect(reverse_lazy('articulos:path_articulo_detalle', kwargs = {'pk': pk_articulo} ))

@login_required
def DeslikearArticulo(request, pk_articulo):
    usuario = request.user
    articulo = Articulo.objects.get(pk = pk_articulo)
    like = LikeArticulo.objects.filter(articulo = articulo, usuario = usuario)
    like.delete()

    return HttpResponseRedirect(reverse_lazy('articulos:path_articulo_detalle', kwargs = {'pk': pk_articulo} ))

def BuscarArticulo(request):
    buscado = request.GET.get('buscado', '').strip()

    if buscado:
        articulos = Articulo.objects.filter(titulo__contains=buscado)

        valor_a_ordenar = request.GET.get('orden', None)
        articulos_ordenados = ordenar_articulos(articulos, valor_a_ordenar)

        articulos_paginados = paginar_articulos(request, articulos_ordenados, 1, 6)[0]
        rango_paginas = paginar_articulos(request, articulos_ordenados, 1, 6)[1]

        ultimos_5 = ultimos_n_por_fecha(5)

        categorias_bd = Categoria.objects.all()
        context = {
            'buscado': buscado,
            'categorias': categorias_bd,
            'articulos_recientes': ultimos_5,
            'articulos_p': articulos_paginados,
            'rango_paginas': rango_paginas,
        }
        return render(request, 'Articulos/blog_busqueda.html', context)

    return HttpResponseRedirect(reverse_lazy('articulos:path_listar_articulos'))