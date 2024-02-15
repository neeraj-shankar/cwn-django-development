from ApiView.models import Category, Author, Post
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    category_names = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = "__all__"
    
    def get_author_name(self, obj):
        return obj.author.name if obj.author else None
    
    def get_category_names(self, obj):
        return [category.name for category in obj.categories.all()]
