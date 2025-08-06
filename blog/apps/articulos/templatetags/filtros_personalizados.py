from django import template

register = template.Library()

MESES_ES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

@register.filter
def nombre_mes(numero):
    """Convierte el número de mes en su nombre en español"""
    return MESES_ES.get(numero, "")