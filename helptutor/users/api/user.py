from rest_framework import generics, status, viewsets, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response

from google.oauth2 import id_token
from google.auth.transport import requests

from utils.error import ValidationError

from helptutor.users.models import User, Tutor
from helptutor.users.serializers import *
from knox.models import AuthToken

import time
import threading


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        send_email()
        return Response({
            "user":
            UserViewSerializer(user, context=self.get_serializer_context()).data,
            "token":
            AuthToken.objects.create(user)[1]
        })

def send_email():
    t1 = threading.Thread(target=time_sleep, )
    t1.start()

def time_sleep():
    print('llamando')
    for i in range(30):
        time.sleep(1)
        print('hola' + str(i))


class LoginGoogleAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        token = request.data['id_token']
        CLIENT_ID = "581408483289-vlrheiceitim0evek4mrjnakqm5v07m7.apps.googleusercontent.com"
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            userid = idinfo['sub']
            user = User.objects.get(email=idinfo['email'])
        except ValueError:
            raise ValidationError('Error auth GoogleAPI')
        except User.DoesNotExist:
            raise ValidationError('Credenciales incorrectas')
        return Response({
            "user":
            UserViewSerializer(user, context=self.get_serializer_context()).data,
            "token":
            AuthToken.objects.create(user)[1]
        })