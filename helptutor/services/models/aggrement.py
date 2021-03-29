from django.db import models

from .contract import Contract

class Aggrement(Contract):
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE, verbose_name='Servicio')
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE, verbose_name='Estudiante')

    class Meta:
        verbose_name = 'Acuerdo'
        verbose_name_plural = 'Acuerdos'



