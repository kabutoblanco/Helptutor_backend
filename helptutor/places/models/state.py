from django.db import models

from utils.models import HelpTutorModel


class State(HelpTutorModel):
    name = models.CharField(max_length=64, verbose_name='Nombre')
    cod = models.CharField(max_length=3, verbose_name='Código')

    country = models.ForeignKey('places.Country', on_delete=models.CASCADE, verbose_name='País')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)