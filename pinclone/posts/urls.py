from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком постов
    path('posts/', views.posts_list),
    # Отдельная страница с информацией 
    path('posts/<pk>/', views.posts_detail),
] 