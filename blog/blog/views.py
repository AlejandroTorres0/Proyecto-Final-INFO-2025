from django.shortcuts import render

def Index(request):    
    return render(request, 'index.html')

def sobre_nosotros(request):
    return render(request, 'Sobre_nosotros.html')

def novedades(request):
    return render(request, 'Novedades.html')

def contactanos(request):
    return render(request, 'contactanos.html')