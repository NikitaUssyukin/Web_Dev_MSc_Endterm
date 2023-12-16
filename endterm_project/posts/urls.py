from django.urls import path
from . import views
from .views import create_post, edit_post, delete_post
from .views import post_list, post_detail

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('<int:pk>/edit/', edit_post, name='edit_post'),
    path('<int:pk>/delete/', delete_post, name='delete_post'),
]