from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from helptutor.advertisements.models import Answer
from helptutor.advertisements.serializers import AnswerSerializer


class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer 
    permission_classes = (IsAuthenticated, )

class AdvertisementAnswerAPIView(generics.ListAPIView):

    serializer_class = AnswerSerializer
    queryset = Answer.objects.filter()
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        queryset = Answer.objects.filter(advertisement=kwargs['pk'])
        data = self.get_serializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)
