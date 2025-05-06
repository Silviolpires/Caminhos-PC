from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import PessoaFisicaForm, PessoaJuridicaForm, EnderecoForm
from .models import PessoaFisica, PessoaJuridica
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from functools import wraps

def login_required(view_func):
    """
    Decorador que verifica se o usuário está autenticado na sessão.
    Se não estiver, redireciona para a página de login.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Verificar se o usuário está autenticado na sessão
        if not request.session.get('is_authenticated', False):
            # Armazenar URL atual para redirecionamento após login
            next_url = request.get_full_path()
            login_url = f"{reverse('home_view:login')}?next={next_url}"
            return redirect(login_url)
        
        # Se estiver autenticado, prossegue para a view
        return view_func(request, *args, **kwargs)
    
    return wrapper



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

# Modifique a classe LoginView para verificar a senha criptografada
class LoginView(TemplateView):
    template_name = 'home_view/login.html'
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Tentar encontrar um usuário com este email
        try:
            # Primeiro tentamos encontrar na tabela de pessoas físicas
            pessoa = PessoaFisica.objects.get(email=email)
            
            # Verificar a senha usando check_password
            if check_password(password, pessoa.password):
                # Login bem-sucedido - Armazenar dados na sessão
                request.session['user_id'] = pessoa.id
                request.session['user_email'] = pessoa.email
                request.session['user_name'] = pessoa.name
                request.session['user_type'] = 'fisica'
                request.session['is_authenticated'] = True
                
                # Redirecionar para o dashboard em vez da home
                return redirect('dashboard:main')
            else:
                # Senha incorreta
                return render(request, self.template_name, {
                    'error_message': 'Senha incorreta.'
                })
                
        except PessoaFisica.DoesNotExist:
            # Se não encontrar como pessoa física, tenta como pessoa jurídica
            try:
                pessoa = PessoaJuridica.objects.get(email=email)
                
                # Verificar a senha
                if check_password(password, pessoa.password):
                    # Login bem-sucedido - Armazenar dados na sessão
                    request.session['user_id'] = pessoa.id
                    request.session['user_email'] = pessoa.email
                    request.session['user_name'] = pessoa.name
                    request.session['user_type'] = 'juridica'
                    request.session['is_authenticated'] = True
                    request.session['business_name'] = pessoa.business_name
                    
                    # Redirecionar para o dashboard em vez da home
                    return redirect('dashboard:main')
                else:
                    # Senha incorreta
                    return render(request, self.template_name, {
                        'error_message': 'Senha incorreta.'
                    })
            except PessoaJuridica.DoesNotExist:
                # Usuário não encontrado em nenhuma tabela
                return render(request, self.template_name, {
                    'error_message': 'E-mail não cadastrado.'
                })
            
# Arquivo: home_view/decorators.py

from django.shortcuts import redirect
from django.urls import reverse
from functools import wraps

def login_required(view_func):
    """
    Decorador que verifica se o usuário está autenticado na sessão.
    Se não estiver, redireciona para a página de login.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Verificar se o usuário está autenticado na sessão
        if not request.session.get('is_authenticated', False):
            # Armazenar URL atual para redirecionamento após login
            next_url = request.get_full_path()
            login_url = f"{reverse('home_view:login')}?next={next_url}"
            return redirect(login_url)
        
        # Se estiver autenticado, prossegue para a view
        return view_func(request, *args, **kwargs)
    
    return wrapper  

# Adicionar à views.py

def logout_view(request):
    """
    View para realizar o logout do usuário, limpando a sessão.
    """
    # Limpar todas as variáveis de sessão relacionadas ao usuário
    keys_to_remove = [
        'user_id', 'user_email', 'user_name', 'user_type',
        'is_authenticated', 'business_name'
    ]
    
    for key in keys_to_remove:
        if key in request.session:
            del request.session[key]
    
    # Redirecionar para a página inicial
    return redirect('home_view:home')          