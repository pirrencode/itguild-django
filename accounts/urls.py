from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginview, name="login"),
    path('logout/', views.logoutview, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('welcome/', views.welcome, name="welcome"),
]
