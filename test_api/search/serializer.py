from rest_framework import serializers
from .models import User, SearchPoint


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("__all__")


class SearchUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchPoint
        fields = '__all__'
