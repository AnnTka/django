from rest_framework import serializers
from django.conf import settings


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(min_length=8, max_length=50)
