from .utils import ultimos_n_por_fecha
from .models import Categoria

def datos_globales_app_articulos(request):
    categorias_bd = Categoria.objects.all()
    ultimos_5 = ultimos_n_por_fecha(5)

    return {
        'categorias':categorias_bd,
        'articulos_recientes': ultimos_5, 
    }