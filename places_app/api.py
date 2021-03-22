from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from .serializers import *
from .models import *


class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountrySerializer


class CountryStatesAPIView(generics.ListAPIView):

    serializer_class = StateSerializer
    queryset = State.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = State.objects.filter(country=kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StateViewSet(viewsets.ModelViewSet):

    queryset = State.objects.filter(is_active=True)
    serializer_class = StateSerializer

    
class StateCitiesAPIView(generics.ListAPIView):

    serializer_class = CitySerializer
    queryset = State.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = City.objects.filter(state=kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.filter(is_active=True)
    serializer_class = CitySerializer

    
class CityUniversitiesAPIView(generics.ListAPIView):

    serializer_class = UniversitySerializer
    queryset = University.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = University.objects.filter(city=kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UniversityViewSet(viewsets.ModelViewSet):

    queryset = University.objects.filter(is_active=True)
    serializer_class = UniversitySerializer
