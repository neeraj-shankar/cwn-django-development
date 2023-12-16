from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='blogger__home-page'),
    path('author/', views.show_author_list, name='blogger__author'),
    path('post/', views.post_management, name='blogger__post')
]