from django.db import models


class Sesion(models.Model):
    duration = models.FloatField(default=0, verbose_name='Duración')

    contract = models.ForeignKey('services.Contract', on_delete=models.CASCADE, verbose_name='Contrato')
    time_slot = models.ForeignKey('schedules.TimeSlot', on_delete=models.CASCADE, verbose_name='Franja')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Sesión'
        verbose_name_plural = 'Sesiones'

    def __str__(self):
        return "[{}] {}".format(self.id, self.contract)