from django.db import models

from .contract import Contract


class Nomination(Contract):
    offer = models.ForeignKey('services.Offer', on_delete=models.CASCADE, verbose_name='Oferta')
    tutor = models.ForeignKey('users.Tutor', on_delete=models.CASCADE, verbose_name='Tutor')

    class Meta:
        verbose_name = 'Postulacion'
        verbose_name_plural = 'Postulaciones'