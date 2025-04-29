from django.urls import path
from . import views

app_name = 'trilhas_view'

urlpatterns = [
    path('', views.lista_trilhas, name='lista_trilhas'),
    path('<int:trilha_id>/', views.detalhe_trilha, name='detalhe_trilha'),
    path('criar/', views.criar_trilha, name='criar_trilha'),
    path('<int:trilha_id>/editar/', views.editar_trilha, name='editar_trilha'),
    path('<int:trilha_id>/excluir/', views.excluir_trilha, name='excluir_trilha'),
]