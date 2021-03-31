from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from helptutor.places.serializers import CountrySerializer
from helptutor.places.models import Country


class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountrySerializer