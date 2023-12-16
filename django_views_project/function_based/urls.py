from django.urls import path
from . import views

urlpatterns = [
    path('create-employee/', views.create_employee, name='function_based__create-employee'),
]