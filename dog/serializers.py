from rest_framework import serializers
from .models import Dog

class DogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id', 'nazwa', 'opis', 'gotowe')
