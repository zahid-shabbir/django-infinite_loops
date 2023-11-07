
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='starting_page'),
    path('posts/', views.posts, name='posts_page'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail_page'),

]
