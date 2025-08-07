from django.core.paginator import Paginator
from .models import Articulo 

def ordenar_articulos(queryset, orden):
    if orden == 'asc':
        return queryset.order_by('creado')
    elif orden == 'desc':
        return queryset.order_by('-creado')
    return queryset

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