from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import User
from ..utils.authentication import encrypt_passwd



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'firstName',
            'lastName',
            'email',
            'password',
            'is_activated',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        firstName = validated_data['firstName']
        lastName = validated_data['lastName']
        email = validated_data['email']
        password = validated_data['password']
        encriptPassword=encrypt_passwd(password)
        print (encriptPassword)
        user_obj = User(
            firstName=firstName,
            lastName=lastName,
            email=email,
            is_activated=True,
            password=encriptPassword)
        user_obj.save()
        return validated_data


