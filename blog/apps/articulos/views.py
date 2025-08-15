from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ArticuloForm, FormularioEditarArticulo
from .models import Articulo, Categoria, LikeArticulo
from .utils import ordenar_articulos, paginar_articulos, obtener_siguiente_anterior, ultimos_n_por_fecha, obtener_n_populares
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden

# Create your views here.
def Listar_Articulos(request):
    # Aquí iría la lógica para listar los artículos

    valor_a_ordenar = request.GET.get('orden', None)
    articulos = Articulo.objects.all()
    articulos_ordenados = ordenar_articulos(articulos, valor_a_ordenar)

    numero_de_articulos_por_pagina = 5

    articulos_paginados = paginar_articulos(request, articulos_ordenados, numero_de_articulos_por_pagina, 6)[0]
    rango_paginas = paginar_articulos(request, articulos_ordenados, numero_de_articulos_por_pagina, 6)[1]

    ultimos_5 = ultimos_n_por_fecha(5)

    #Base
    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]

    categorias_bd = Categoria.objects.all()
    context = {
        'articulos_populares': populares,
        'articulos_populares_footer': articulos_populares_footer,

        'categorias':categorias_bd,
        'articulos_recientes': ultimos_5,
        'articulos_p': articulos_paginados,
        'rango_paginas': rango_paginas
    }

    return render(request, 'articulos/blog.html', context)

def Filtrar_Categoria(request, pk):
    categoria_filtrada = Categoria.objects.get(pk = pk)

    articulos_filtrados = Articulo.objects.filter(categoria = categoria_filtrada)

    ultimos_5 = ultimos_n_por_fecha(5)

    #Base
    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]

    valor_a_ordenar = request.GET.get('orden', None)
    articulos_ordenados = ordenar_articulos(articulos_filtrados, valor_a_ordenar)

    numero_de_articulos_por_pagina = 5

    articulos_paginados = paginar_articulos(request, articulos_ordenados, numero_de_articulos_por_pagina, 6)[0]
    rango_paginas = paginar_articulos(request, articulos_ordenados, numero_de_articulos_por_pagina, 6)[1]

    categorias_bd = Categoria.objects.all()

    context = {
            'articulos_populares': populares,
            'articulos_populares_footer': articulos_populares_footer,
            'categorias': categorias_bd,
            'articulos_p': articulos_paginados,
            'articulos_recientes': ultimos_5,
            'id_categoria': categoria_filtrada.id,
            'nombre_categoria': categoria_filtrada.nombre,
            'rango_paginas': rango_paginas
    }

    return render(request, 'articulos/blog.html', context)

def Detalle_Articulo(request, pk):
    articulo = Articulo.objects.get(pk = pk)

    articulo_anterior, articulo_siguiente = obtener_siguiente_anterior(articulo)

    #Base
    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]

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
            'articulos_populares': populares,
            'articulos_populares_footer': articulos_populares_footer,

            'comentarios': comentarios,
            'categorias': categorias_bd,
            'articulo': articulo,
            'articulos_recientes': ultimos_5,
            'articulo_anterior':  articulo_anterior,
            'articulo_siguiente': articulo_siguiente
    }

    return render(request, 'articulos/detalles_blog.html', context)

@login_required
def Crear_Articulo(request):
    #Base
    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]

    if request.method == 'POST' and request.user.is_staff:
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.usuario = request.user  # Asigna el usuario actual
            articulo.save()
            return HttpResponseRedirect(reverse_lazy('articulos:path_listar_articulos'))
    else:
        form = ArticuloForm()
    context = {
        'form': form,
        'articulos_populares': populares,
        'articulos_populares_footer': articulos_populares_footer
    }
    return render(request, 'articulos/crear_articulo.html', context)

class EditarArticulo(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Articulo
    form_class = FormularioEditarArticulo
    template_name = 'articulos/editar_articulo.html'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    def get_success_url(self):
        return reverse_lazy('articulos:path_articulo_detalle', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        populares = obtener_n_populares(5)
        articulos_populares_footer = populares[:3]

        context['articulos_populares'] = populares
        context['articulos_populares_footer'] = articulos_populares_footer
        return context

class EliminarArticulo(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Articulo
    template_name = 'articulos/eliminar_articulo.html'

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

        numero_de_articulos_por_pagina = 5

        articulos_paginados = paginar_articulos(request, articulos_ordenados, numero_de_articulos_por_pagina, 6)[0]
        rango_paginas = paginar_articulos(request, articulos_ordenados, numero_de_articulos_por_pagina, 6)[1]

        ultimos_5 = ultimos_n_por_fecha(5)

        #Base
        populares = obtener_n_populares(5)
        articulos_populares_footer = populares[:3]

        categorias_bd = Categoria.objects.all()
        context = {
            'articulos_populares': populares,
            'articulos_populares_footer': articulos_populares_footer,
            'buscado': buscado,
            'categorias': categorias_bd,
            'articulos_recientes': ultimos_5,
            'articulos_p': articulos_paginados,
            'rango_paginas': rango_paginas,
        }
        return render(request, 'articulos/blog_busqueda.html', context)

    return HttpResponseRedirect(reverse_lazy('articulos:path_listar_articulos'))