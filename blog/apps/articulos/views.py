from django.shortcuts import render
from .models import Articulo
# Create your views here.

def Listar_Articulos(request):
    # Aquí iría la lógica para listar los artículos
    MESES = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }

    articulos_bd = Articulo.objects.all()

    return render(request, 'articulos/blog.html', {'articulos':articulos_bd, 'meses': MESES})

