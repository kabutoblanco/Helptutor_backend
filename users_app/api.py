from rest_framework import generics, viewsets

from google.oauth2 import id_token
from google.auth.transport import requests

from utils.string_random import get_random_string

from users_app.serializers import TutorSerializer
from users_app.models import Tutor

class TutorViewSet(viewsets.ModelViewSet):

    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()


class TutorGoogleViewSet(viewsets.ModelViewSet):

    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.data)
        object_google = request.data['object_google']
        request.data['password'] = get_random_string(8)
        request.data['username'] = object_google['profileObj']['email'].split('@')[0]
        request.data['first_name'] = object_google['profileObj']['givenName']
        request.data['last_name'] = object_google['profileObj']['familyName']
        request.data['email'] = object_google['profileObj']['email']
        request.data['telephone'] = '123'
        return super().create(request, *args, **kwargs)
