from app.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    enrollment = serializers.IntegerField()
    stream = serializers.CharField(max_length=50)
    university = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.enrollment = validated_data.get('enrollment', instance.enrollment)
        instance.stream = validated_data.get('stream', instance.stream)
        instance.university = validated_data.get('university', instance.university)
        return instance

    
    # Field Level Validation --> Making sure name only accepts alphabetical characters
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("The name must be only alphabets without any spaces.")
        return value

