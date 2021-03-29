from rest_framework import generics, viewsets

from helptutor.advertisements.models import Answer
from helptutor.advertisements.serializers import AnswerSerializer


class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer 