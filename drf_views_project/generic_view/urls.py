from django.urls import path, include
from generic_view import author
from rest_framework.routers import DefaultRouter
from generic_view.author import AuthorListView
from generic_view import posts

# # Creating the router instance
# router = DefaultRouter()

# # Registering the views to with router instance
# router.register(r'author-list', AuthorListView, basename='generic_view-author-list')
# router.register(r'author-create', author.AuthorCreateView, basename='generic_view-author-create')
# router.register(r'authors', author.AuthorUpdateView, basename='generic_view-author-update')
# router.register(r'authors', author.AuthorRetrieveView, basename='generic_view-author-retrieve')
# router.register(r'authors', author.AuthorDestroyView, basename='generic_view-author-destroy')

urlpatterns = [
    path('author/', author.AuthorListView.as_view(), name='generic_view-author-list'),
    path('author/<int:pk>/retrieve/', author.AuthorRetrieveView.as_view(), name='generic_view-author-retrieve'),
    path('author/<int:pk>/update/', author.AuthorUpdateView.as_view(), name='generic_view-author-update'),
    path('author/<int:pk>/destroy/', author.AuthorDestroyView.as_view(), name='generic_view-author-destroy'),
    path('book/create/', posts.BookCreateListView.as_view(), name='generic_view-book-create'),
]