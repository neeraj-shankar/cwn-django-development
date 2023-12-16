from function_based.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    # max_digits determines the maximum number of digits that can be stored, including both the integer and fractional parts.
    # decimal_places specifies the number of decimal places to store. max value --> "999999.99"
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    hire_date = serializers.DateField() # YYYY-MM-DD
