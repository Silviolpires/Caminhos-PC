from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('forumOne/<int:pk>/', views.forumOne, name='forum_one'), 
    path('forumOne/<int:post_id>/like/', views.like_post, name='like_post'),
    path('formulario/', views.criar_post, name='criar_post'),
]