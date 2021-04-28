from rest_framework import serializers

from helptutor.services.models import Offer


class OfferModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'title':instance.title,
            'description':instance.description,
            'student':instance.student.user.first_name,
            'knowledgeArea_Student':instance.knowledgeArea_Student.knowledge_area.name
        }
 
class OfferCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
