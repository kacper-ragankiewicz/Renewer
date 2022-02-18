from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DogSerializers
from .models import Dog

# Create your views here.

class DogView(viewsets.ModelViewSet):
    serializer_class = DogSerializers
    queryset = Dog.objects.all()

