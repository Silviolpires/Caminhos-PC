from django.urls import path
from . import views

urlpatterns = [
    path('', views.ForumView.as_view(), name='forum'),
    path('forumOne', views.ForumView.as_view(), name='forumOne'),  # URL raiz do aplicativo forum
]