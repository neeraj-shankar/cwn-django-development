from rest_framework import serializers

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, unique=True)
    origin = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=50, unique=True)
    bio = serializers.TextField()

