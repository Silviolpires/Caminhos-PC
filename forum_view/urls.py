from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.forum, name='forum'),
    path('forumOne/<int:pk>/', views.forumOne, name='forumOne'), 
    path('forumOne/<int:post_id>/like/', views.like_post, name='like_post'),
    path('formulario/', views.criar_post, name='criar_post'),
]