from django.db import models

from utils.models import HelpTutorModel


class Advertisement(HelpTutorModel):
    title = models.CharField(max_length=64, verbose_name='Titulo')
    description = models.CharField(max_length=120, verbose_name='Descripción')

    student = models.ForeignKey(
        'users.Student', 
        on_delete=models.CASCADE, 
        verbose_name='Estudiante'
    )

    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'

    def __str__(self):
        return "[{}] {}".format(self.id, self.title)