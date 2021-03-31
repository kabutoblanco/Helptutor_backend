from rest_framework import generics, viewsets

from helptutor.advertisements.models import Advertisement
from helptutor.advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer