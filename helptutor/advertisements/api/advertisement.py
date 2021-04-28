from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from helptutor.advertisements.models import Advertisement
from helptutor.advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class StudentAdvertisementAPIView(generics.ListAPIView):
 
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.filter(is_active=True)

    def list(self, request, *args, **kwargs):
        queryset = Advertisement.objects.filter(student=kwargs['pk'], is_active=True)
        data = self.get_serializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)
