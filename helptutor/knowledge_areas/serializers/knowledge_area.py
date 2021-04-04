from rest_framework import serializers

from helptutor.knowledge_areas.models import KnowledgeArea


class KnowledgeAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeArea
        fields = '__all__'