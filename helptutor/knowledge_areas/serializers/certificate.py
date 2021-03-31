from rest_framework import serializers

from helptutor.knowledge_areas.models import Certificate


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = '__all__'
