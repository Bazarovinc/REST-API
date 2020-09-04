from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("__all__")


class SearchUsersSerializer(serializers.Serializer):
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    k = serializers.IntegerField(min_value=1)
    m = serializers.IntegerField(min_value=0)

