from rest_framework import generics, viewsets
from .serializers import CountrySerializer, StateSerializer, CitySerializer, UniversitySerializer
from .models import Country, State, City, University
from rest_framework.response import Response


class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StateViewSet(viewsets.ModelViewSet):

    queryset = State.objects.all()
    serializer_class = StateSerializer

    def retrieve(self, request, pk=None):
        queryset = State.objects.filter(country = pk)
        serializer = StateSerializer(queryset, many=True)
        return Response(serializer.data)


class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer

    def retrieve(self, request, pk=None):
        queryset = City.objects.filter(state = pk)
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)


class UniversityViewSet(viewsets.ModelViewSet):

    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    def retrieve(self, request, pk=None):
        queryset = University.objects.filter(city = pk)
        serializer = UniversitySerializer(queryset, many=True)
        return Response(serializer.data)
