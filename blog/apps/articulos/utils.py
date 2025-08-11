from django.core.paginator import Paginator
from .models import Articulo 
from django.db.models import Count 

ORDENES = {
    'fecha-asc': ['creado'],
    'fecha-dsc': ['-creado'],
    'cat-asc': ['categoria'],
    'cat-dsc': ['-categoria'],
    'fecha-cat-asc': ['creado', 'categoria'],
    'fecha-cat-dsc': ['-creado', '-categoria'],
    'titulo-asc': ['titulo', '-creado'],
    'titulo-dsc': ['-titulo', '-creado'],
}

def ordenar_articulos(queryset, orden):
    orden_predeterminado = 'fecha-dsc'
    campos = ORDENES.get(orden)
    if campos:
        return queryset.order_by(*campos)
    else: 
        #Cuando no se le pasa orden por la url
        campos = ORDENES.get(orden_predeterminado)
        return queryset.order_by(*campos)

def paginar_articulos(request, queryset, por_pagina=1, tamano_bloque=6):
    p = Paginator(queryset, por_pagina)
    page = request.GET.get('page')
    articulos_paginados = p.get_page(page)

    total_paginas = p.num_pages
    pagina_actual = articulos_paginados.number

    principio_bloque = ((pagina_actual - 1) // tamano_bloque) * tamano_bloque + 1
    final_bloque = min(principio_bloque + tamano_bloque, total_paginas + 1)
    rango_paginas = range(principio_bloque, final_bloque)

    return articulos_paginados, rango_paginas

def obtener_siguiente_anterior(articulo_actual):
    try:
        anterior = Articulo.objects.filter(id__lt=articulo_actual.id).order_by('-id').first()
    except Articulo.DoesNotExist:
        anterior = None

    try:
        siguiente = Articulo.objects.filter(id__gt=articulo_actual.id).order_by('id').first()
    except Articulo.DoesNotExist:
        siguiente = None

    return anterior, siguiente

def ultimos_n_por_fecha(num_articulos):
    return Articulo.objects.order_by('-creado')[:num_articulos]

def obtener_n_populares(num_populares):
    #return Articulo.objects.order_by('-likes')[:num_populares] #Devuelve el orden en el que di like, como por fecha, no por cantidad de likes
    return Articulo.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:num_populares]

def obtener_n_portada(num_portada):
    return Articulo.objects.annotate(num_likes=Count('likes')).order_by('-num_likes', '-creado')[:num_portada]