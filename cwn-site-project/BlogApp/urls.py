from django.urls import path
from BlogApp import views 

urlpatterns = [
    #*******************************Category Urls*************************************
    path('category', views.CategoryView, name='category_page' ),
    path('category/add-new', views.AddCategoryView, name='add_category_page'),
    path('category/edit/<cat_id>', views.EditCategoryView, name='edit_category_page'),


    #*******************************Post Urls*************************************
    
    path('posts', views.PostListView, name="post_list_page"),
    path('post/add-new', views.AddPostView, name='add_post_page'),
    path('post/edit/<post_id>', views.EditPostView, name='edit_post_page'),
    path('article/<post_id>', views.PostDetailView, name="post_detail_page"),
    
    path('category/<str:cats>/',views.CategorizedListView, name='categorized_post_page'),
   

    
]