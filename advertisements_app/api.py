from rest_framework import generics, viewsets
from .serializers import (
    AdvertisementSerializer,
    AnswerSerializer,
)
from .models import (
    Advertisement,
    Answer,
)

class AdvertisementViewSet(viewsets.ModelViewSet):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer 
