from django.urls import path
from . import views

app_name = 'home_view'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('user-type/', views.UserTypeView.as_view(), name='user_type'),
    path('cadastro/pessoa-fisica/', views.PfSignUpView.as_view(), name='pf_signup'),
    path('cadastro/pessoa-juridica/', views.PjSignUpView.as_view(), name='pj_signup'),
    path('amigos/', views.FriedsListView.as_view(), name='friends_list'),
    path('login/', views.LoginView.as_view(), name='login'),
]
