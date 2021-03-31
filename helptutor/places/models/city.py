from django.db import models

from utils.models import HelpTutorModel


class City(HelpTutorModel):
    name = models.CharField(max_length=64, verbose_name='Nombre')

    state = models.ForeignKey('places.State', on_delete=models.CASCADE, verbose_name='Departamento')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)