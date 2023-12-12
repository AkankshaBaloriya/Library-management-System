from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_signup, name='register'),
    path('logout/', views.user_logout, name="logout"),
]