from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_view.urls')),
    path('forum/', include ('forum_view.urls')),  # Incluindo as URLs do aplicativo home_view
]