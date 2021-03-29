from django.db import models

from utils.models import HelpTutorModel


class Content(HelpTutorModel):
    name = models.CharField(max_length=64, verbose_name='Nombre')
    file = models.FileField(upload_to='contents', verbose_name='Archivo')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    knowledge_area_tutor = models.ForeignKey(
        'knowledge_areas.KnowledgeArea_Tutor', 
        on_delete=models.CASCADE, 
        verbose_name='Especialidad tutor'
    )

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)