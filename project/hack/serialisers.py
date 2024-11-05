from .models import *
from rest_framework import serializers

class dataSerialiser(serializers.ModelSerializer):
    class Meta:
        model= data
        fields='__all__'