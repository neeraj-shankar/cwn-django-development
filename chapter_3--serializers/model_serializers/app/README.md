# Validation in used in Serializers

### Ovierview
1. When deserializing data, you always need to call is_valid() before attempting to access the validated data, or save an object instance. 
2. If any validation errors occur, the .errors property will contain a dictionary representing the resulting error messages
3. Each key in the dictionary will be the field name, and the values will be lists of strings of any error messages corresponding to that field. 
4. The non_field_errors key may also be present, and will list any general validation errors.
5. The name of the non_field_errors key may be customized using the NON_FIELD_ERRORS_KEY REST framework setting.


### The .is_valid() method takes an optional raise_exception flag that will cause it to raise a serializers.ValidationError exception if there are validation errors.
```
# Return a 400 response if the data was invalid.
serializer.is_valid(raise_exception=True)
```

### Field Level Validation
- This type of validation checks the validity of individual fields in the serializer.
```
Syntax: validate_<field_name>

class MySerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Name must contain only alphabetic characters.")
        return value

```
### Object-level validation
- This type of validation checks the validity of the entire object based on multiple fields.
```
class MySerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')

        if start_date > end_date:
            raise serializers.ValidationError("End date must be after start date.")

        return attrs

```

### Unique validation:
- This type of validation checks whether a field's value is unique within a certain context.
```
class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['name', 'email']
        extra_kwargs = {
            'name': {'validators': []},  # To disable default unique validation
            'email': {'unique': True}  # To enforce uniqueness of email field
        }

```

### Custom validation methods
- These methods can be named anything and are invoked explicitly from within the serializer's validate() method.

```
class MySerializer(serializers.ModelSerializer):
    def validate(self, data):
        self.validate_custom_logic(data)
        return data

    def validate_custom_logic(self, data):
        # Custom validation logic here
        pass

```