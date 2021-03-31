from django.db import models

from utils.models import HelpTutorModel


class Schedule(HelpTutorModel):
    tutor = models.ForeignKey('users.Tutor', on_delete=models.CASCADE, verbose_name='Tutor')

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return "[{}] {}".format(self.id, self.tutor)