from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class FormularioRegistroUsuario(UserCreationForm):       
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    	
    def __init__(self, *args, **kwargs):
        super(FormularioRegistroUsuario, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Obligatorio. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_</small></span>'

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['first_name'].label = ''
        self.fields['first_name'].widget.attrs['max_length'] = 100    

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['last_name'].label = ''
        self.fields['last_name'].widget.attrs['max_length'] = 100

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo Electrónico'
        self.fields['email'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña no puede ser demasiado similar a tu otra información personal.</li><li>Tu contraseña debe contener al menos 8 caracteres.</li><li>Tu contraseña no puede ser una contraseña de uso común.</li><li>Tu contraseña no puede ser completamente numérica.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Introduce la misma contraseña que antes, para verificación.</small></span>'    