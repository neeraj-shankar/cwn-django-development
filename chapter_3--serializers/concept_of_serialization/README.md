# Basic Concept Serializers

### Python JSON package
#### Python has built in package called json which can be used to deal with json data. 
1. dumps(data)--> converts a python object to a json string
2. loads(data)--> parse a json string to python object

### Serializer in DRF
- Serializers allow complex data such as querysets and model instances to be converted to native. Python datatypes that can then be easily rendered into JSON, XML or other content types. 
- Serializers also provide deserialization, allowing parsed data to be converted back into complex types
- The serializers in REST framework work very similarly to Django's Form and ModelForm classes.
