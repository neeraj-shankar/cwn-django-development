from app.models import Student
from rest_framework import serializers
import logging
import re

logger = logging.getLogger("app")


# custom validation fields
def limit_roll_count(value):
    logger.info(f"Field Level Validation of Enrollment: {value} started")
    if value > 1000:
        raise serializers.ValidationError(f"Sorry Maximum Capacity is 1000")
    return value


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    enrollment = serializers.IntegerField(validators=[limit_roll_count])
    stream = serializers.CharField(max_length=50)
    university = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.enrollment = validated_data.get("enrollment", instance.enrollment)
        instance.stream = validated_data.get("stream", instance.stream)
        instance.university = validated_data.get("university", instance.university)
        return instance

    # Field Level Validation --> Making sure name only accepts alphabetical characters
    def validate_name(self, value):
        logger.info(f"Field Level Validation of name: {value} started")
        # Regular expression to match only alphabets and white spaces
        pattern = r"^[a-zA-Z\s]+$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "The name must be only alphabets and spaces."
            )
        return value
