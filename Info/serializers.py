from rest_framework import serializers
from .models import User

class UserSrlzr(serializers.Serializer):
    class Meta:
        model = User
        fields = ['num','greet','email','name','city']
    
    def create(self, validated_data):
        user = User.objects.create(
            greet = validated_data['greet'],
            email=validated_data['email'],
            name=validated_data['name'],
            num=validated_data['num'],
            city=validated_data['city']
        )
        return user
