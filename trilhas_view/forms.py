from django import forms
from .models import Trilha

class TrilhaForm(forms.ModelForm):
    class Meta:
        model = Trilha
        fields = ['nome', 'descricao', 'distancia', 'duracao', 'nivel_dificuldade', 'guias']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'duracao': forms.TimeInput(attrs={'type': 'time'}),
            'guias': forms.CheckboxSelectMultiple(),
        }