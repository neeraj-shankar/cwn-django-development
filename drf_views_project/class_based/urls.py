from django.urls import path
from .views import CategoryRetrieveUpdateDeleteView, CategoryCreateListView

urlpatterns = [
    path('create-list/', CategoryCreateListView.as_view(), name="class_based--create-list"),
    path('create-list/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name="class_based--create-list"),
]