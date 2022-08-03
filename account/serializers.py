from dataclasses import fields
import email
from pyexpat import model
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

# we are writing this because we need cofirm password field in our Registration Request


    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)


    class Meta:
        model =  User
        fields = ['email', 'name', 'password', 'password2', 'tc' ]
        extra_kwargs = {
            'password':{'write_only':True}
        }


# Validating Password and Confirm Password while Registration       attrs=data

    def validate(self, attrs):

        password = attrs.get('password')
        password2 = attrs.get('password2')
        
        if password != password2:
            raise serializers.ValidationError('Password and Confirm Password Doesnot match.')


        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)




class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField( max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']