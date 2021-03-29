from django.db import models

from utils.models import HelpTutorModel


class Classroom(HelpTutorModel):
    link = models.CharField(max_length=120, verbose_name='Link')

    sesion = models.ForeignKey('sesions.Sesion', on_delete=models.CASCADE, verbose_name='Sesión')

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

    def __str__(self):
        return "[{}] {}".format(self.id, self.sesion)
