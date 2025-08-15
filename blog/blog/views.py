from django.shortcuts import render
from apps.articulos.utils import obtener_n_populares, ultimos_n_por_fecha, obtener_n_portada
from apps.articulos.models import Articulo
from apps.categorias.models import Categoria

def Index(request):
    populares = obtener_n_populares(5)
    primeros_populares = populares[:2]

    recientes = ultimos_n_por_fecha(5)

    articulos_portada = obtener_n_portada(5)

    articulos_populares_footer = populares[:3]

    articulos_aleatorios = Articulo.objects.order_by('?')[:4]

    context = {
        'articulos_populares': populares,
        'articulos_populares_footer': articulos_populares_footer,

        'articulos_recientes': recientes,
        'articulos_aleatorios': articulos_aleatorios,
        'primeros_dos_populares': primeros_populares,
        'articulos_portada': articulos_portada,
    }
    return render(request, 'index.html', context)

def sobre_nosotros(request):

    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]

    context = {
        'articulos_populares': populares,
        'articulos_populares_footer': articulos_populares_footer,
    }
    return render(request, 'sobre_nosotros.html', context)

def novedades(request):
    categorias_bd = Categoria.objects.all()[:5]

    populares = obtener_n_populares(5)
    articulos_populares_footer = obtener_n_populares(3)

    categorias_con_articulos = []

    for categoria in categorias_bd:
        articulos = Articulo.objects.filter(categoria=categoria).order_by('-creado')[:4]
        categorias_con_articulos.append({
            'categoria': categoria,
            'articulos': articulos
        })

    context = {
        'categorias': categorias_bd,
        'categorias_con_articulos': categorias_con_articulos,
        'articulos_populares': populares,
        'articulos_populares_footer': articulos_populares_footer
    }
    return render(request, 'novedades.html', context)