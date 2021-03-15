from django.db import models

from users_app.models import Tutor

# Create your models here.
class Schedule(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, verbose_name='Tutor')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return "[{}] {}".format(self.id, self.tutor)


class TimeSlot(models.Model):
    day = models.DateField(verbose_name='Día')
    start_time = models.TimeField(verbose_name='Hora de inicio')
    end_time = models.TimeField(verbose_name='Hora de fin')
    is_editabled = models.BooleanField(default=True, verbose_name='¿Es editable?')
    is_busy = models.BooleanField(default=False, verbose_name='¿Es ocupado?')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name='Horario')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Franja'
        verbose_name_plural = 'Franjas'

    def __str__(self):
        return "[{}] {} {} {}".format(self.id, self.day, self.start_time, self.end_time)