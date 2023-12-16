from django.urls import path
from blogApp import views
urlpatterns = [
    path('create-permission/', views.create_permission, name="blogApp__create-permission"),
]