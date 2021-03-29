from django.db import models

from utils.models import HelpTutorModel


class Contract(HelpTutorModel):
    is_accepted_tutor = models.BooleanField(default=False, verbose_name='¿Es aceptado por el tutor?')
    is_accepted_student = models.BooleanField(default=False, verbose_name='¿Es aceptado por el estudiante?')
    price = models.FloatField(default=0, verbose_name='Precio')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.is_accepted_tutor, self.is_accepted_student)