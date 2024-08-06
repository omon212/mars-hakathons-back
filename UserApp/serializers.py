from rest_framework import serializers
from Calculator.models import *
import random


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeModel
        fields = ['id', 'home_owner', 'home_address', 'phone_number', 'password']


class HomeDatasSRL(serializers.ModelSerializer):
    class Meta:
        model = HomeModel
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    home_id = serializers.IntegerField()
    password = serializers.CharField(max_length=16)



