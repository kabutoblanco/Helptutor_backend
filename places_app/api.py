from rest_framework import generics, viewsets
from .serializers import CountrySerializer, StateSerializer, CitySerializer, UniversitySerializer
from .models import Country, State, City, University


class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StateViewSet(viewsets.ModelViewSet):

    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer


class UniversityViewSet(viewsets.ModelViewSet):

    queryset = University.objects.all()
    serializer_class = UniversitySerializer
