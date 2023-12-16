from django.contrib import admin
from .models import Category, Author, Post, Comment

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ['name', 'origin', 'email', 'bio']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'content', 'author', 'publication_date']