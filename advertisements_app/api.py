from rest_framework import generics, viewsets

from .models import *
from .serializers import *


class AdvertisementViewSet(viewsets.ModelViewSet):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer 
