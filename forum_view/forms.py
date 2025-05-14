from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'tipo', 'descricao', 'imagem']

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite um título',
                'required': True,
                'id': 'titulo',
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select',
                'id': 'tipo',
                'required': True,
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'cols': 50,
                'required': True,
                'id': 'descricao',
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'id': 'imagem',
            }),
        }
