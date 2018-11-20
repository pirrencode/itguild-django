from django.urls import path
from .import views
from django.conf.urls.static import static

app_name = 'events'

urlpatterns = [
    path('events/', views.events, name="events"),
]
