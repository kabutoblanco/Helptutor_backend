from rest_framework import serializers

from helptutor.users.models import User, Tutor
from .user import UserCreateSerializer, UserUpdateSerializer, UserViewSerializer

# google services oauth
from google.oauth2 import id_token
from google.auth.transport import requests

from utils.string import get_random_string
from utils.error import ValidationError


class TutorViewSerializer(serializers.ModelSerializer):
    user = UserViewSerializer(read_only=True)

    class Meta:
        model = Tutor
        fields = '__all__'


class TutorCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(write_only=True)

    class Meta:
        model = Tutor
        fields = '__all__'

    def validate_user(self, data):
        """Validated user isnt tutor."""
        email = data['email']
        tutor = Tutor.objects.filter(user__email=email)
        if tutor.exists() and self.context.get('create', True):
            raise ValidationError('Ya existe tutor')
        return data

    def validate(self, data):
        """Validated user is exist."""
        data['user'] = get_or_create_user(data['user'])
        return data


class TutorUpdateSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer(write_only=True)

    class Meta:
        model = Tutor
        fields = '__all__'


class TutorGoogleCreateSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, data):
        """Validate token Google"""
        token = data
        CLIENT_ID = "581408483289-vlrheiceitim0evek4mrjnakqm5v07m7.apps.googleusercontent.com"
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            user = self.get_information_google(dict(), idinfo)
            tutor = Tutor.objects.filter(user__email=user['email'])
            if tutor.exists():
                raise ValidationError('Ya existe tutor')
            return data
            self.context['user'] = get_or_create_user(user)
        except ValueError:
            raise ValidationError('Error auth GoogleAPI')
        except User.DoesNotExist:
            raise ValidationError('Credenciales incorrectas')
        return data

    def create(self, validated_data):
        validated_data.pop('token')

        validated_data['user'] = self.context['user']

        tutor = Tutor.objects.create(**validated_data)
        tutor.save()

        return tutor

    def get_information_google(self, data, idinfo, *args, **kwargs):      
        data['email'] = idinfo['email']
        data['first_name'] = idinfo['given_name']
        data['last_name'] = idinfo['family_name']        
        data['password'] = get_random_string(8)
        return data


def get_or_create_user(data):
    try:
        user = User.objects.get(email=data['email'])
    except User.DoesNotExist:
        email = data['email']
        data['username'] = data['email']
        user = User.objects.create(**data)
        user.set_password(data['password'])
        user.save()
        data.pop('username')
    return user