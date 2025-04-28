from django.urls import path
from . import views

app_name = 'home_view'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tipo-usuario/', views.UserTypeView.as_view(), name='user_type'),
    path('cadastro/pf/', views.PfSignUpView.as_view(), name='pf_signup'),
    path('cadastro/pj/', views.PjSignUpView.as_view(), name='pj_signup'),
    path('cadastro/juridica/', views.cadastro_juridica, name='cadastro_juridica'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('parceiros/', views.FriedsListView.as_view(), name='friends_list'),
]