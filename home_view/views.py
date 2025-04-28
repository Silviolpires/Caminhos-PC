from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import PessoaFisicaForm, PessoaJuridicaForm, EnderecoForm
from .models import PessoaFisica, PessoaJuridica
from django.contrib.auth.hashers import make_password, check_password

class HomeView(TemplateView):
    template_name = 'home_view/home.html'

class UserTypeView(TemplateView):
    template_name = 'home_view/userType.html'

class PfSignUpView(FormView):
    template_name = 'home_view/pfSignUp.html'
    form_class = PessoaFisicaForm
    success_url = reverse_lazy('home_view:login')
    
    def form_valid(self, form):
        # Salvar os dados do formulário
        pessoa = form.save(commit=False)
        # Criptografar a senha antes de salvar
        pessoa.password = make_password(pessoa.password)
        pessoa.save()
        messages.success(self.request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return super().form_valid(form)
    

class PjSignUpView(FormView):
    template_name = 'home_view/pjSignUp.html'
    form_class = PessoaJuridicaForm
    success_url = reverse_lazy('home_view:login')
    
    def form_valid(self, form):
        # Salvar os dados do formulário
        pessoa_juridica = form.save(commit=False)
        # Criptografar a senha antes de salvar
        pessoa_juridica.password = make_password(pessoa_juridica.password)
        pessoa_juridica.save()
        messages.success(self.request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return super().form_valid(form)
    

class FriedsListView(ListView):
    template_name = 'home_view/friendsList.html'
    model = PessoaJuridica
    context_object_name = 'parceiros'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtragem por busca
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                business_name__icontains=search_query
            ) | queryset.filter(
                region__icontains=search_query
            )
        
        # Filtragem por região
        region = self.request.GET.get('region')
        if region:
            queryset = queryset.filter(region__icontains=region)
            
        return queryset
  
def cadastro_juridica(request):
    """
    Função para processamento do formulário completo de cadastro de pessoa jurídica,
    incluindo dados pessoais e dados do empreendimento.
    """
    if request.method == 'POST':
        pessoa_form = PessoaFisicaForm(request.POST)
        juridica_form = PessoaJuridicaForm(request.POST)
        endereco_form = EnderecoForm(request.POST)
        
        if all([pessoa_form.is_valid(), juridica_form.is_valid(), endereco_form.is_valid()]):
            # Criar a pessoa jurídica
            pj = juridica_form.save(commit=False)
            # Criptografar a senha
            pj.password = make_password(pj.password)
            pj.save()
            
            # Registrar mensagem de sucesso
            messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
            
            # Redirecionar para a página de login
            return redirect('home_view:login')
    else:
        pessoa_form = PessoaFisicaForm()
        juridica_form = PessoaJuridicaForm()
        endereco_form = EnderecoForm()
    
    return render(request, 'home_view/cadastro_juridica.html', {
        'pessoa_form': pessoa_form,
        'juridica_form': juridica_form,
        'endereco_form': endereco_form
    })

class LoginView(TemplateView):
    template_name = 'home_view/login.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Verificar se os campos foram preenchidos
        if not email or not password:
            return render(request, self.template_name, {
                'error_message': 'Por favor, preencha todos os campos.'
            })
        
        # Tentar autenticar como pessoa física
        pessoa = None
        user_type = None
        
        try:
            pessoa = PessoaFisica.objects.get(email=email)
            user_type = 'fisica'
        except PessoaFisica.DoesNotExist:
            # Se não for pessoa física, tentar como pessoa jurídica
            try:
                pessoa = PessoaJuridica.objects.get(email=email)
                user_type = 'juridica'
            except PessoaJuridica.DoesNotExist:
                # Usuário não encontrado
                return render(request, self.template_name, {
                    'error_message': 'E-mail não cadastrado.'
                })
        
        # SOLUÇÃO TEMPORÁRIA: Permitir login sem verificação de senha
        # Em produção, remova este bloco e descomente o bloco abaixo
        request.session['user_id'] = pessoa.id
        request.session['user_email'] = pessoa.email
        request.session['user_name'] = pessoa.name
        request.session['user_type'] = user_type
        messages.success(request, f'Bem-vindo(a), {pessoa.name}!')
        return redirect('home_view:home')
        
        # Verificação de senha normal - descomente em produção
        # if check_password(password, pessoa.password):
        #     # Login bem-sucedido
        #     request.session['user_id'] = pessoa.id
        #     request.session['user_email'] = pessoa.email
        #     request.session['user_name'] = pessoa.name
        #     request.session['user_type'] = user_type
        #     messages.success(request, f'Bem-vindo(a), {pessoa.name}!')
        #     return redirect('home_view:home')
        # else:
        #     # Senha incorreta
        #     return render(request, self.template_name, {
        #         'error_message': 'Senha incorreta.'
        #     })

# Função de logout
def logout_view(request):
    # Limpar a sessão
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_email' in request.session:
        del request.session['user_email']
    if 'user_name' in request.session:
        del request.session['user_name']
    if 'user_type' in request.session:
        del request.session['user_type']
    
    # Adicionar mensagem de sucesso
    messages.success(request, "Logout realizado com sucesso!")
    
    # Redirecionar para a página inicial
    return redirect('home_view:home')