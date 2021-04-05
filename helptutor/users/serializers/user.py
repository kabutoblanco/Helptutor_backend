# Django
from django.contrib.auth import authenticate

# rest_framework
from rest_framework import serializers

# google
from google.oauth2 import id_token
from google.auth.transport import requests

# models
from helptutor.users.models import User
from knox.models import AuthToken


class UserViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'gender', 'birthday', 'telephone', 'photo')
        

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('user_permissions', 'groups', )

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('username', 'email', 'password', 'user_permissions', 'groups', )
        

# - - - - - Section login - - - - -
class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True)
    user = UserViewSerializer(read_only=True)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            self.context['user'] = user
            return data
        raise serializers.ValidationError("Credenciales incorrectas")

    def create(self, validated_data):
        instance = dict()
        user = self.context['user']
        instance['user'] = user
        instance['token'] = AuthToken.objects.create(user)[1]
        return instance
    
    def to_representation(self, value):
        value['user'] = UserViewSerializer(value['user']).data
        return value


class LoginGoogleSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, data):
        """Validate token Google"""
        token = data
        CLIENT_ID = "581408483289-vlrheiceitim0evek4mrjnakqm5v07m7.apps.googleusercontent.com"
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            userid = idinfo['sub']
            user = User.objects.get(email=idinfo['email'])
            self.context['user'] = user
        except ValueError:
            raise ValidationError('Error auth GoogleAPI')
        except User.DoesNotExist:
            raise ValidationError('Credenciales incorrectas')
        return data
    
    def create(self, validated_data):
        instance = dict()
        user = self.context['user']
        instance['user'] = user
        instance['token'] = AuthToken.objects.create(user)[1]
        return instance
    
    def to_representation(self, value):
        value['user'] = UserViewSerializer(value['user']).data
        return value