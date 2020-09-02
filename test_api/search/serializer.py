from rest_framework import serializers
from .models import User, SearchPoint


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    description = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.x = validated_data.get('x', instance.x)
        instance.y = validated_data.get('y', instance.y)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class SearchUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchPoint
        fields = '__all__'
