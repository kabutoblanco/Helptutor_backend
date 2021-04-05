from rest_framework import serializers

from helptutor.knowledge_areas.models import KnowledgeArea_Tutor
from .knowledge_area import KnowledgeAreaSerializer


class KnowledgeArea_TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeArea_Tutor
        fields = '__all__'

    def validate_knowledge_area(self, data):
        """Validated knowledge area isnt record active"""
        request = KnowledgeArea_Tutor.objects.filter(knowledge_area=data, is_active=True)
        if request.exists():
            raise serializers.ValidationError('Ya existe una especilidad registrada')
        return data


class KnowledgeArea_TutorViewSerializer(serializers.ModelSerializer):
    knowledge_area = KnowledgeAreaSerializer(read_only=True)

    class Meta:
        model = KnowledgeArea_Tutor
        fields = '__all__'