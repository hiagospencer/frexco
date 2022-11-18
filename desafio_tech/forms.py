from django import forms
from desafio_tech.models import Usuario

class MeuFormulario(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = '__all__'