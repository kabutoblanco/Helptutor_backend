from rest_framework import generics, status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response

from google.oauth2 import id_token
from google.auth.transport import requests

from utils.exception import CustomException
from utils.string_random import get_random_string

from .models import User, Tutor
from .serializers import *


class TutorViewSet(viewsets.ModelViewSet):

    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()

    def create(self, request, *args, **kwargs):
        email = request.data['email']
        hd = request.data['email'].split('@')[1]
        request.data['username'] = email.split('@')[0] + hd.split('.')[0]
        tutor = create_tutor(request, self.get_serializer_class())
        return Response(
            TutorViewSerializer(
                tutor, context=self.get_serializer_context()).data,
            status=status.HTTP_201_CREATED
        )
    
    def partial_update(self, request, pk=None):
        tutor = update_tutor(request, TutorUpdateSerializer, **{'pk': pk})
        return Response(
            TutorViewSerializer(
                tutor, context=self.get_serializer_context()).data,
        )

    def list(self, request):
        return Response(
            TutorViewSerializer(
                self.queryset, many=True).data,
        )

    def retrieve(self, request, pk=None):
        try:
            queryset = Tutor.objects.get(user=pk)
        except Tutor.DoesNotExist:
            raise CustomException('Tutor no existe', 'detail', status.HTTP_409_CONFLICT)
        return Response(
            TutorViewSerializer(
                queryset, context=self.get_serializer_context()).data,
        )


class TutorGoogleViewSet(viewsets.ModelViewSet):

    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()

    def create(self, request, *args, **kwargs):
        token = request.data['id_token']
        CLIENT_ID = "581408483289-vlrheiceitim0evek4mrjnakqm5v07m7.apps.googleusercontent.com"
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            userid = idinfo['sub']
            request.data['password'] = get_random_string(8)
            request.data['username'] = idinfo['email'].split('@')[0] + idinfo['email'].split('@')[1].split('.')[0]
            request.data['first_name'] = idinfo['given_name']
            request.data['last_name'] = idinfo['family_name']
            request.data['email'] = idinfo['email']
            tutor = create_tutor(request, self.get_serializer_class())    
        except ValueError:
            raise CustomException('Error auth GoogleAPI', 'detail', status.HTTP_409_CONFLICT)
        return Response(
            TutorViewSerializer(
                tutor, context=self.get_serializer_context()).data,
            status=status.HTTP_201_CREATED
        )    


def create_tutor(request, *args, **kwargs):
    #validators
    try:
        user = User.objects.get(email=request.data['email'])
        if user.is_tutor():
            raise CustomException('Tutor duplicado', 'detail', status.HTTP_409_CONFLICT)
    #user
    except User.DoesNotExist:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
    request.data['user'] = user.pk
    #tutor
    serializer = args[0](data=request.data)
    serializer.is_valid(raise_exception=True)
    tutor = serializer.save()
    return tutor


def update_tutor(request, *args, **kwargs):
    #validators
    try:
        user = User.objects.get(pk=kwargs['pk'])
        if not user.is_tutor():
            raise CustomException('Tutor no existe', 'detail', status.HTTP_409_CONFLICT)
        else:
            serializer = UserUpdateSerializer(data=request.data, instance=user)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
    #user
    except User.DoesNotExist:
        raise CustomException('Usuario no existe', 'detail', status.HTTP_409_CONFLICT)
    #tutor
    tutor = Tutor.objects.get(user=user)
    serializer = args[0](data=request.data, instance=tutor)
    serializer.is_valid(raise_exception=True)
    tutor = serializer.save()
    return tutor
