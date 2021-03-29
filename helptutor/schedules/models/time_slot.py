from django.db import models

from utils.models import HelpTutorModel


class TimeSlot(HelpTutorModel):
    day = models.DateField(verbose_name='Día')
    start_time = models.TimeField(verbose_name='Hora de inicio')
    end_time = models.TimeField(verbose_name='Hora de fin')
    is_editabled = models.BooleanField(default=True, verbose_name='¿Es editable?')
    is_busy = models.BooleanField(default=False, verbose_name='¿Es ocupado?')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    schedule = models.ForeignKey('schedules.Schedule', on_delete=models.CASCADE, verbose_name='Horario')

    class Meta:
        verbose_name = 'Franja'
        verbose_name_plural = 'Franjas'

    def __str__(self):
        return "[{}] {} {} {}".format(self.id, self.day, self.start_time, self.end_time)