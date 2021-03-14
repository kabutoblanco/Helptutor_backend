from django.db import models

from schedules_app.models import TimeSlot
from services_app.models import Contract

# Create your models here.
class Sesion(models.Model):
    duration = models.FloatField(default=0, verbose_name='Duración')

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='Contrato')
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, verbose_name='Franja')

    is_active = models.BooleanField(verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Sesión'
        verbose_name_plural = 'Sesiones'

    def __str__(self):
        return "[{}] {}".format(self.id, self.contract)


class Classroom(models.Model):
    link = models.CharField(max_length=120, verbose_name='Link')

    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE, verbose_name='Sesión')

    is_active = models.BooleanField(verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

    def __str__(self):
        return "[{}] {}".format(self.id, self.sesion)


class Chat(models.Model):
    log = models.FileField(upload_to='chats', verbose_name='Log')

    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE, verbose_name='Sesión')

    is_active = models.BooleanField(verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

    def __str__(self):
        return "[{}] {}".format(self.id, self.sesion)


class Qualification(models.Model):
    score = models.IntegerField(default=0, verbose_name='Puntuación')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE, verbose_name='Sesión')

    is_active = models.BooleanField(verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Calificacion'
        verbose_name_plural = 'Calificaciones'

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.sesion, self.score)