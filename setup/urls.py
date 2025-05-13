from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_view.urls')),
    path('forum/', include ('forum_view.urls')),  # Incluindo as URLs do aplicativo home_view
    path('trilhas/', include('trilhas_view.urls')), # Aplicativo trilhas_view
    path('dashboard/', include('dashboard.urls')), # Aplicativo dashboard
    
 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)