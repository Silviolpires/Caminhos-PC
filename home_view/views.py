from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import PessoaFisicaForm, PessoaJuridicaForm, EnderecoForm
from .models import PessoaFisica, PessoaJuridica
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from functools import wraps
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError


def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        print("DECORADOR: is_authenticated =", request.session.get('is_authenticated'))
        if not request.session.get('is_authenticated', False):
            next_url = request.get_full_path()
            login_url = f"{reverse('home_view:login')}?next={next_url}"
            return redirect(login_url)
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
        pessoa = form.save(commit=False)
        raw_password = pessoa.password
        pessoa.password = make_password(pessoa.password)
        pessoa.save()

        User.objects.create_user(
            username=pessoa.email,
            email=pessoa.email,
            password=raw_password
        )

        messages.success(self.request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return super().form_valid(form)


class FriedsListView(ListView):
    template_name = 'home_view/friendsList.html'
    model = PessoaJuridica
    context_object_name = 'parceiros'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                business_name__icontains=search_query
            ) | queryset.filter(
                region__icontains=search_query
            )
        region = self.request.GET.get('region')
        if region:
            queryset = queryset.filter(region__icontains=region)
        return queryset


from django.contrib.auth.models import User
from django.db import IntegrityError

def cadastro_juridica(request):
    if request.method == 'POST':
        pessoa_form = PessoaFisicaForm(request.POST)
        juridica_form = PessoaJuridicaForm(request.POST)
        endereco_form = EnderecoForm(request.POST)

        if all([pessoa_form.is_valid(), juridica_form.is_valid(), endereco_form.is_valid()]):
            pj = juridica_form.save(commit=False)
            password = juridica_form.cleaned_data['password']  # usar cleaned_data
            pj.password = make_password(password)
            pj.save()

            try:
                if not User.objects.filter(username=pj.email).exists():
                    User.objects.create_user(
                        username=pj.email,
                        email=pj.email,
                        password=password
                    )
            except IntegrityError:
                messages.warning(request, "Este e-mail já está em uso no sistema.")

            messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
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

    def post(self, request, *args, **kwargs):
        request.session['is_authenticated'] = True
        print("Sessão autenticada:", request.session['is_authenticated'])
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            pessoa = PessoaFisica.objects.get(email=email)
            if check_password(password, pessoa.password):
                
                request.session['user_email'] = pessoa.email
                request.session['user_name'] = pessoa.name
                request.session['user_type'] = 'fisica'
                user = authenticate(request, username=pessoa.email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard:main')
            else:
                return render(request, self.template_name, {'error_message': 'Senha incorreta.'})
        except PessoaFisica.DoesNotExist:
            try:
                pessoa = PessoaJuridica.objects.get(email=email)
                if check_password(password, pessoa.password):
                    request.session['user_id'] = pessoa.id
                    request.session['user_email'] = pessoa.email
                    request.session['user_name'] = pessoa.name
                    request.session['user_type'] = 'juridica'
                    request.session['is_authenticated'] = True
                    request.session['business_name'] = pessoa.business_name
                    print("Sessão salva:")
                    print("is_authenticated =", request.session.get('is_authenticated'))  # ⬅️ Verifique isso no terminal

                    return redirect('/dashboard/')

                else:
                    return render(request, self.template_name, {'error_message': 'Senha incorreta.'})
            except PessoaJuridica.DoesNotExist:
                return render(request, self.template_name, {'error_message': 'E-mail não cadastrado.'})


def logout_view(request):
    keys_to_remove = [
        'user_id', 'user_email', 'user_name', 'user_type',
        'is_authenticated', 'business_name'
    ]
    for key in keys_to_remove:
        if key in request.session:
            del request.session[key]
    return redirect('home_view:home')
