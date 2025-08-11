from django.shortcuts import render
from apps.articulos.utils import obtener_n_populares, ultimos_n_por_fecha, obtener_n_portada
from apps.articulos.models import Articulo

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
    return render(request, 'Sobre_nosotros.html')

def novedades(request):
    return render(request, 'Novedades.html')

def contactanos(request):
    return render(request, 'contactanos.html')