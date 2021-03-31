from django.db import models

from utils.models import HelpTutorModel


class Answer(models.Model):
    likes = models.IntegerField(default=0, verbose_name='Me gusta')
    description = models.CharField(max_length=120, verbose_name='Descripción')

    advertisement = models.ForeignKey(
        'advertisements.Advertisement', 
        on_delete=models.CASCADE, 
        verbose_name='Anuncio'
    )
    user = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE, 
        verbose_name='Usuario'
    )

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return "[{}]".format(self.id)