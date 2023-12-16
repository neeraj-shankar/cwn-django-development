from django.urls import path
from MemberApp import views

urlpatterns = [
    path('login', views.LoginView, name= 'login_page'),
    path('logged-out', views.LogoutView,name='logout_page'),
    path('registration', views.RegisterView, name='register_page')
]