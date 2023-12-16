from django.contrib import admin
from django.db import models
from django.db.models import fields
from BlogApp.models import Category, Author, Post, Comment

# Register your models here.
admin.site.register(Author)

#********************************* Admin Page Customization for Post Category*******************
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    # To display field names for category 
    fields = ('img','title', 'desc', 'slug')

    # Shows the multiple coulmns on Category page-admin
    list_display = ('title', 'slug')

    # add search field option for the category page
    search_fields= ('title',)

    # Provide filter option 
    list_filter = ('title',)

    # ordering 
    ordering = ('title',)

#********************************* Admin Page Customization for Post List*******************
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # To display the fields to add post in post list
    fields = ('title', 'category', 'author', 'img', 'slug', 'desc')

    # Show the multiple columns on admin page of PostList
    list_display = ('title', 'date', )

    #add search field option for post lists
    search_fields = ('title', 'author')

    # list_filter - adding filter option
    list_filter = ('title', 'author')

    # ordernig 
    ordering =('date', 'title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
     # To display the fields to add post in post list
    fields = ('post', 'name', 'email', 'desc', 'parent')

    # Show the multiple columns on admin page of PostList
    list_display = ('name', 'email', )

    #add search field option for post lists
    search_fields = ('name', 'email')

    # list_filter - adding filter option
    list_filter = ('name', 'email')

    # ordernig 
    ordering =('email', 'timestamp')