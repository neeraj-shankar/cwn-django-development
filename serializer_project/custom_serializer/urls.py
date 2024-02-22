from django.urls import path
from .authors import AuthorList, AuthorDetail
from .test_nested_serializer import NestedSerializerView

urlpatterns = [
    path('author/', AuthorList.as_view(), name='ApiView__author-view'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='ApiView__author-view'),
    path('nested-serializer/', NestedSerializerView.as_view(), name='nested-serializer' )

]