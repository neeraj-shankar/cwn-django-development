from rest_framework import serializers
from .models import Author, Book
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'bio']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested serializer

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
