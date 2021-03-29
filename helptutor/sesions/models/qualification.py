from django.db import models


class Qualification(models.Model):
    score = models.IntegerField(default=0, verbose_name='Puntuación')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    sesion = models.ForeignKey('sesions.Sesion', on_delete=models.CASCADE, verbose_name='Sesión')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Calificacion'
        verbose_name_plural = 'Calificaciones'

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.sesion, self.score)