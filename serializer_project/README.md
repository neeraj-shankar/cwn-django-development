## Serializers

### Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types

### Field Level Validation
`Field-level validation in serializers by defining custom validation methods for individual fields. These validation methods allow you to validate the data for a specific field before it is saved or processed further.`

### Object-level validation
`Object-level validation in Django REST Framework (DRF) allows you to perform validation that involves multiple fields or the object as a whole. Unlike field-level validation, which focuses on validating individual fields, object-level validation considers the object as a whole and may involve interactions between multiple fields.`

### Custom Validators for individual field(s)
#### Individual fields on a serializer can include validators, by declaring them on the field instance, for example:

```
def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

class GameRecord(serializers.Serializer):
    score = serializers.IntegerField(validators=[multiple_of_ten])
```

#### Serializer classes can also include reusable validators that are applied to the complete set of field data. These validators are included by declaring them on an inner Meta class, like so:

```
class EventSerializer(serializers.Serializer):
    name = serializers.CharField()
    room_number = serializers.IntegerField(choices=[101, 102, 103, 201])
    date = serializers.DateField()

    class Meta:
        # Each room only has one event per day.
        validators = [
            UniqueTogetherValidator(
                queryset=Event.objects.all(),
                fields=['room_number', 'date']
            )
        ]
```