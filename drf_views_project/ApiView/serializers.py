from rest_framework import serializers
from .models import Author, Post, Category
from utils.logger import setup_logger

log = setup_logger(__name__)

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    origin = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=50)
    bio = serializers.CharField()

    # Custom validation for the 'name' field
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "Name must only contain alphabetic characters."
            )
        return value

    # Object level validation for the 'name' and 'bio field'
    def validate(self, attrs):

        name = attrs.get("name")
        bio = attrs.get("bio")

        if name.lower() == bio.lower():
            raise serializers.ValidationError("Name and Bio cannot be same")
        return attrs

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.origin = validated_data.get("origin", instance.origin)
        instance.email = validated_data.get("email", instance.email)
        instance.bio = validated_data.get("bio", instance.bio)
        instance.save()

        return instance


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "categories"]

    def create(self, validated_data):
        author_data = validated_data.pop("author")
        categories_data = validated_data.pop("categories")

        # Check if the author already exists
        author_name = author_data.get("name")
        author, _ = Author.objects.get_or_create(name=author_name, defaults=author_data)

        # Create or get existing categories
        categories = []
        for category_data in categories_data:
            log.info(f"Category Data: {categories_data}")
            category_name = category_data.get("name")
            category, _ = Category.objects.get_or_create(name=category_name, defaults=category_data)
            categories.append(category)

        # Create the post with the associated author and categories
        post = Post.objects.create(author=author, **validated_data)
        post.categories.set(categories)

        return post


    def update(self, instance, validated_data):
        author_data = validated_data.pop("author")
        categories_data = validated_data.pop("categories")

        author = instance.author
        author.name = author_data.get("name", author.name)
        author.save()

        instance.title = validated_data.get("title", instance.title)
        instance.save()

        categories = [
            Category.objects.create(**category_data)
            for category_data in categories_data
        ]
        instance.categories.set(categories)

        return instance
