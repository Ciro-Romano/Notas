from django import forms
from .models import Nota

class FormNotas(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'descripcion']