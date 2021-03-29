from django.db import models

from utils.models import HelpTutorModel


class KnowledgeArea_Student(HelpTutorModel):
    knowledge_area = models.ForeignKey(
        'knowledge_areas.KnowledgeArea', 
        on_delete=models.CASCADE, 
        verbose_name='Área de conocimiento'
    )
    student = models.ForeignKey(
        'users.Student', 
        on_delete=models.CASCADE, 
        verbose_name='Estudiante'
    )

    class Meta:
        verbose_name = 'Interes'
        verbose_name_plural = 'Intereses'

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.knowledge_area, self.student)