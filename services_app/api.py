from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Service,
    Offer,
    Contract,
    Aggrement,
    Nomination,
)

from .serializers import (
    ServiceSerializer,
    OfferSerializer,
    ContractSerializer,
    AggrementSerializer,
    NominationSerializer
)

class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.filter(is_active = True)
    serializer_class = ServiceSerializer

class OfferViewSet(viewsets.ModelViewSet):

    queryset = Offer.objects.filter(is_active = True)
    serializer_class = OfferSerializer

class ContractViewSet(viewsets.ModelViewSet):

    queryset = Contract.objects.filter(is_active = True)
    serializer_class = ContractSerializer

class AggrementViewSet(viewsets.ModelViewSet):

    queryset = Aggrement.objects.filter(is_active = True)
    serializer_class = AggrementSerializer

class NominationViewSet(viewsets.ModelViewSet):

    queryset = Nomination.objects.filter(is_active = True)
    serializer_class = NominationSerializer
