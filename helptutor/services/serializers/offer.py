from rest_framework import serializers

from helptutor.services.models import Offer


class OfferModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class OfferCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'