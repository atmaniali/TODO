#serialize 
from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
