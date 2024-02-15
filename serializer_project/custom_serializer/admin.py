from django.contrib import admin
from custom_serializer.models import Author, Category, Post, Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)