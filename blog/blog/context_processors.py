from  apps.articulos.utils import obtener_n_populares

def datos_globales(request):
    populares = obtener_n_populares(5)
    articulos_populares_footer = populares[:3]

    return {
        "articulos_populares": populares,
        "articulos_populares_footer": articulos_populares_footer 
    }