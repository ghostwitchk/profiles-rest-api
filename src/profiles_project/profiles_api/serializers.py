from rest_framework import serializers




class HelloSerializer(serializers.Serializer):
    """ selrialzes a name field for testing our API"""


    name = serializers.CharField(max_length=10)
