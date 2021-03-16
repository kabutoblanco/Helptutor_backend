from rest_framework import generics, viewsets
from .serializers import (
    PaymentSerializer
)
from .models import (
    Payment
)

class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
