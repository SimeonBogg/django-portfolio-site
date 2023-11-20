from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="home"),
    path('post/', views.post, name="home"),
    path('profile/', views.profile, name="home"),
]