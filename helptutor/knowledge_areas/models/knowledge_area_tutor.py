from django.db import models

from utils.models import HelpTutorModel


class KnowledgeArea_Tutor(HelpTutorModel):    
    tags = models.CharField(max_length=120, blank=True, verbose_name="Tags")
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    knowledge_area = models.ForeignKey(
        'knowledge_areas.KnowledgeArea', 
        on_delete=models.CASCADE, 
        verbose_name='Área de conocimiento'
    )
    tutor = models.ForeignKey(
        'users.Tutor', 
        on_delete=models.CASCADE, 
        verbose_name='Tutor'
    )

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.knowledge_area, self.tutor)