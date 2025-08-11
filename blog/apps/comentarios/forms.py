from django import forms 
from .models import Comentario

class FormularioEditarComentario(forms.ModelForm): 
	class Meta:
		model = Comentario
		fields = ['contenido']  
		widgets = {
			'contenido': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Escribe tu comentario...'
			})
		}