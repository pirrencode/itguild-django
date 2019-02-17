from django.urls import path
from .import views
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('gallery/', views.rss, name="gallery"),
    path('about/', views.about, name="about"),
    path('rss/', views.rss, name="rss"),
    path('team/', views.team, name="team"),
    path('manifesto/', views.manifesto, name="manifesto"),
    path('create/', views.create, name="create"),
    path('<int:pk>/upvote/', views.upvote, name="upvote"),
    path('<int:pk>/downvote/', views.downvote, name="downvote"),
    path('user/<int:fk>/', views.userposts, name="userposts"),
    #path('<int:pk>/upvote', views.upvote, name="upvote"),
    #path('posts/(?P<post_id>[0-9]+)/$', views.home),
    #path('posts/<int:post_id>/', posts.views.post_details, name="post_details"),

]
