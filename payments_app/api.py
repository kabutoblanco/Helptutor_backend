from rest_framework import generics, viewsets

from .models import *
from .serializers import *


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
