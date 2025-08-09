from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'imagen', 'contenido', 'categoria', 'resumen', 'slug']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Título'}),
            'contenido': forms.Textarea(attrs={'class': 'single-input', 'placeholder': 'Contenido'}),
            'resumen': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Resumen'}),
            'slug': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Slug'}),
        }

class FormularioEditarArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'imagen', 'contenido', 'categoria', 'resumen'] 
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Título'}),
            'contenido': forms.Textarea(attrs={'class': 'single-input', 'placeholder': 'Contenido'}),
            'resumen': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Resumen'}),
        }