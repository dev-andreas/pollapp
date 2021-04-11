from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from accounts.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']
        read_only_fields = ['date_joined']