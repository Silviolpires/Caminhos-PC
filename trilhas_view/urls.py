from django.urls import path
from . import views

app_name = 'trilhas_view'

urlpatterns = [
    path('', views.lista_trilhas, name='lista_trilhas'),
    path('<int:trilha_id>/', views.detalhe_trilha, name='detalhe_trilha'),
]