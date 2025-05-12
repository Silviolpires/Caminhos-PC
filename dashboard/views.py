# dashboard/views.py

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView
from home_view.views import login_required
from django.utils.decorators import method_decorator
from home_view.models import PessoaFisica, PessoaJuridica
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# View principal do dashboard
@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard/main.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = 'main'
        context['breadcrumbs'] = []
        
        # Dados específicos baseados no tipo de usuário
        if self.request.session.get('user_type') == 'fisica':
            user_id = self.request.session.get('user_id')
            # Você pode adicionar qualquer dado relevante para pessoa física
            # context['dados_especificos'] = ...
        elif self.request.session.get('user_type') == 'juridica':
            user_id = self.request.session.get('user_id')
            # Você pode adicionar qualquer dado relevante para pessoa jurídica
            # context['dados_especificos'] = ...
            
        return context

# View de perfil do usuário
@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'dashboard/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = 'profile'
        context['breadcrumbs'] = [{'title': 'Meu Perfil', 'url': None}]
        
        # Buscar dados do usuário baseado no tipo
        user_id = self.request.session.get('user_id')
        user_type = self.request.session.get('user_type')
        
        if user_type == 'fisica':
            try:
                context['usuario'] = PessoaFisica.objects.get(pk=user_id)
            except PessoaFisica.DoesNotExist:
                # Tratar caso o usuário não exista mais
                pass
        elif user_type == 'juridica':
            try:
                context['usuario'] = PessoaJuridica.objects.get(pk=user_id)
            except PessoaJuridica.DoesNotExist:
                # Tratar caso o usuário não exista mais
                pass
                
        return context

# View para pessoas físicas - minhas trilhas
@method_decorator(login_required, name='dispatch')
class MinhasTrilhasView(TemplateView):
    template_name = 'dashboard/minhas_trilhas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = 'minhas_trilhas'
        context['breadcrumbs'] = [{'title': 'Minhas Trilhas', 'url': None}]
        
        # Verificar se o usuário é pessoa física
        if self.request.session.get('user_type') != 'fisica':
            return redirect('dashboard:main')
            
        # Aqui você pode buscar as trilhas associadas ao usuário
        # context['trilhas'] = ...
            
        return context

# View para pessoas jurídicas - meu empreendimento
@method_decorator(login_required, name='dispatch')
class MeuEmpreendimentoView(TemplateView):
    template_name = 'dashboard/meu_empreendimento.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = 'meu_empreendimento'
        context['breadcrumbs'] = [{'title': 'Meu Empreendimento', 'url': None}]
        
        # Verificar se o usuário é pessoa jurídica
        if self.request.session.get('user_type') != 'juridica':
            return redirect('dashboard:main')
            
        # Buscar dados do empreendimento
        user_id = self.request.session.get('user_id')
        try:
            context['empreendimento'] = PessoaJuridica.objects.get(pk=user_id)
        except PessoaJuridica.DoesNotExist:
            # Tratar caso o empreendimento não exista mais
            pass
            
        return context

# View para estatísticas de pessoas jurídicas
@method_decorator(login_required, name='dispatch')
class EstatisticasView(TemplateView):
    template_name = 'dashboard/estatisticas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = 'estatisticas'
        context['breadcrumbs'] = [{'title': 'Estatísticas', 'url': None}]
        
        # Verificar se o usuário é pessoa jurídica
        if self.request.session.get('user_type') != 'juridica':
            return redirect('dashboard:main')
            
        # Adicionar estatísticas relevantes
        # context['estatisticas'] = ...
            
        return context