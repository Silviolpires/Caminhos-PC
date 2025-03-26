from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'tipo', 'descricao', 'imagem']

        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Digite um título',
                'required': True,
                'id': 'titulo',
            }),
            'tipo': forms.Select(attrs={
                'id': 'tipo',
                'required': True,
            }),
            'descricao': forms.Textarea(attrs={
                'rows': 4,
                'cols': 50,
                'required': True,
                'id': 'descricao',
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'accept': 'image/*',
                'id': 'imagem',
            }),
        }