from django.db import models

from utils.models import HelpTutorModel


class KnowledgeArea(HelpTutorModel):
    name = models.CharField(max_length=64, verbose_name='Nombre')
    level = models.IntegerField(default=0, verbose_name='Nivel')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    knowledge_area = models.ManyToManyField('self', blank=True, verbose_name='Especialidades')

    class Meta:
        verbose_name = 'Area de conocimiento'
        verbose_name_plural = 'Areas de conocimientos'

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.level, self.name)



 





