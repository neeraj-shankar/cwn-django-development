from django.urls import path
from ApiView.authors import AuthorList, AuthorDetail
from ApiView.category import CategoryList, CategoryDetail
from ApiView.post import PostList, PostDetail

urlpatterns = [
    path('category/', CategoryList.as_view(), name='ApiView__category-list' ),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='ApiView__category-detail' ),
    path('author/', AuthorList.as_view(), name='ApiView__author-view'),
    path('author/<int:pk>', AuthorDetail.as_view(), name='ApiView__author-view'),
    path('post/', PostList.as_view(), name='ApiView__post_list'),
    path('post/<int:pk>', PostDetail.as_view(), name='ApiView__post_detail'),
    path('posts/delete/', PostDetail.as_view(), name='post-delete-multiple'),

    
]