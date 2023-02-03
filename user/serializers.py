from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserLoginandRegisterSerializer(serializers.Serializer):

    username = serializers.CharField(required = True,max_length = 150,error_messages = {
        "required" : "Please Enter User Name !",
        "max_length" : "Entred User Name is too long",
    })

    password = serializers.CharField(required = True,min_length = 8,max_length = 150,error_messages = {
        "required" : "Please Enter Password",
        "max_length" : "Entred Password is too long",
        "min_length" : "Password should be more than 8 characters",
    })

class UserRegisterSerializer(serializers.Serializer):

    @property
    def user(self) -> User:
        return self.__user

    def create(self, validated_data):
        self.__user = User(**validated_data)
        return self.__user
    

class UserLoginSerializer(serializers.Serializer):

    def validate(self, attrs:dict):
        self.__user = User.objects.filter(username = attrs.get("username")).first()

        if not self.__user:
            raise serializers.ValidationError("There is not user with entred username")
        
        if not check_password(attrs.get("password"),self.__user.password):
            raise serializers.ValidationError("Password is wrong :(")
        
        return attrs
        
    @property
    def token(self) -> str:
        return Token.objects.get_or_create(user = self.__user)[0].key
    
    @property
    def user(self) -> User:
        return self.__user
