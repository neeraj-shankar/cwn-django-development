from django.urls import path
from ApiView.views import CategoryView
from ApiView.authors import AuthorView

urlpatterns = [
    path('category/', CategoryView.as_view(), name='ApiView__category-view' ),
    path('author/', AuthorView.as_view(), name='ApiView__author-view')
]