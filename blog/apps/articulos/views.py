from django.shortcuts import render

# Create your views here.

def Listar_Articulos(request):
    # Aquí iría la lógica para listar los artículos
    return render(request, 'articulos/blog.html')

