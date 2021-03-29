from rest_framework import serializers

from helptutor.knowledge_areas.models import KnowledgeArea_Tutor
from .knowledge_area import KnowledgeAreaViewSerializer


class KnowledgeArea_TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeArea_Tutor
        fields = '__all__'


class KnowledgeArea_TutorViewSerializer(serializers.ModelSerializer):
    knowledge_area = KnowledgeAreaViewSerializer(read_only=True)

    class Meta:
        model = KnowledgeArea_Tutor
        fields = '__all__'