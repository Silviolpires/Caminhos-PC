from django import forms
from .models import PessoaFisica, PessoaJuridica

class PessoaFisicaForm(forms.ModelForm):
    password_confirm = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(),
        max_length=255
    )
    
    class Meta:
        model = PessoaFisica
        fields = [
            'name', 'rg', 'cpf', 'birth_date', 'cep', 
            'phone', 'email', 'password'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "As senhas não coincidem")
        
        return cleaned_data


class PessoaJuridicaForm(forms.ModelForm):
    password_confirm = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(),
        max_length=255
    )
    
    class Meta:
        model = PessoaJuridica
        fields = [
            'name', 'rg', 'cpf', 'birth_date', 'phone', 'email', 'password',  # Adicionados os campos do responsável
            'business_name', 'cnpj', 'address', 'region',
            'business_phone', 'business_email', 'social_media'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),  # Widget para data
            'password': forms.PasswordInput(),
            'social_media': forms.Textarea(attrs={'rows': 3}),
            'address': forms.Textarea(attrs={'rows': 2}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "As senhas não coincidem")
        
        return cleaned_data


class EnderecoForm(forms.Form):
    """
    Formulário simples para endereço sem cardinalidade com os modelos.
    Este campo é apenas informativo.
    """
    logradouro = forms.CharField(max_length=255, label='Logradouro')
    numero = forms.CharField(max_length=10, label='Número')
    complemento = forms.CharField(max_length=255, label='Complemento', required=False)
    bairro = forms.CharField(max_length=100, label='Bairro')
    cidade = forms.CharField(max_length=100, label='Cidade')
    estado = forms.CharField(max_length=2, label='Estado')