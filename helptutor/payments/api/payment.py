from rest_framework import generics, viewsets

from helptutor.payments.models import Payment
from helptutor.payments.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
