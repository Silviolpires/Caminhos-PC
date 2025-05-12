# dashboard/urls.py

from django.urls import path
from . import views
from .views import DashboardView

app_name = 'dashboard'

urlpatterns = [
    # View principal do dashboard
    path('', DashboardView.as_view(), name='main'),
    
    # Perfil do usuário
    path('perfil/', views.ProfileView.as_view(), name='profile'),
    
    # Rotas para pessoa física
    path('minhas-trilhas/', views.MinhasTrilhasView.as_view(), name='minhas_trilhas'),
    
    # Rotas para pessoa jurídica
    path('meu-empreendimento/', views.MeuEmpreendimentoView.as_view(), name='meu_empreendimento'),
    path('estatisticas/', views.EstatisticasView.as_view(), name='estatisticas'),
]