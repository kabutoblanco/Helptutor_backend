from rest_framework import generics, status, viewsets
from rest_framework.authentication import BasicAuthentication

from google.oauth2 import id_token
from google.auth.transport import requests

from utils.string_random import get_random_string
from utils.exception import CustomException

from users_app.serializers import TutorSerializer
from users_app.models import Tutor

class TutorViewSet(viewsets.ModelViewSet):

    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()

    def create(self, request, *args, **kwargs):
        email = request.data['email']
        hd = request.data['email'].split('@')[1]
        request.data['username'] = email.split('@')[0] + hd.split('.')[0]
        return super().create(request, *args, **kwargs)


class TutorGoogleViewSet(viewsets.ModelViewSet):

    authentication_classes = (BasicAuthentication, )
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()

    def create(self, request, *args, **kwargs):
        token = request.data['id_token']
        CLIENT_ID = "581408483289-vlrheiceitim0evek4mrjnakqm5v07m7.apps.googleusercontent.com"
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            userid = idinfo['sub']
            request.data['password'] = get_random_string(8)
            request.data['username'] = idinfo['email'].split('@')[0] + idinfo['hd'].split('.')[0]
            request.data['first_name'] = idinfo['given_name']
            request.data['last_name'] = idinfo['family_name']
            request.data['email'] = idinfo['email']        
        except ValueError:
            raise CustomException('No se registro tutor', 'detail', status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
