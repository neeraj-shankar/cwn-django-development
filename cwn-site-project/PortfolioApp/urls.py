from django.urls import path
from PortfolioApp import views

urlpatterns = [
    path('', views.HomeView, name='home_page'),
    path('contact', views.ContactView,name='contact_page'),
    
]