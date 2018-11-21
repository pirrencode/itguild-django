from django.urls import path, include
from . import views
from django.conf.urls.static import static

app_name = 'events'

urlpatterns = [
    path('events/', views.events, name="events"),
    path('eventcreate/', views.eventcreate, name="eventcreate"),
    path('<int:event_id>', views.detail, name="detail"),
    #path('detail/', views.detail, name="detail"),
]
