from django.contrib import admin
from django.urls import include, path
from posts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('events/', include('events.urls')),
    path('', views.home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
