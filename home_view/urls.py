from django.urls import path
from . import views
from .views import LoginView

app_name = 'home_view'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('user-type/', views.UserTypeView.as_view(), name='user_type'),
    path('cadastro/pessoa-fisica/', views.PfSignUpView.as_view(), name='pf_signup'),
    path('cadastro/pessoa-juridica/', views.cadastro_juridica, name='pj_signup'),
    path('amigos/', views.FriedsListView.as_view(), name='friends_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
