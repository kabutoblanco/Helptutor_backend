from rest_framework import serializers

from .models import (
    Service,
    Offer,
    Contract,
    Aggrement,
    Nomination,
)
 

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'

class AggrementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aggrement
        fields = '__all__'

class NominationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nomination
        fields = '__all__'
