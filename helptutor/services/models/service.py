from django.db import models

from utils.models import HelpTutorModel


class Service(HelpTutorModel):
    title = models.CharField(max_length=64, verbose_name='Titulo')
    price = models.FloatField(default=0, verbose_name='Precio')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    tutor = models.ForeignKey('users.Tutor', on_delete=models.CASCADE, verbose_name='Tutor')
    knowledgeArea_Tutor = models.ForeignKey('knowledge_areas.KnowledgeArea_Tutor', on_delete=models.CASCADE, verbose_name='Area de conocimiento')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return "[{}] {}".format(self.id, self.title)