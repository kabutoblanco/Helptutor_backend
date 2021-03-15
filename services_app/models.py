from django.db import models

from users_app.models import Tutor, Student

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=64, verbose_name='Titulo')
    price = models.FloatField(default=0, verbose_name='Precio')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, verbose_name='Tutor')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return "[{}] {}".format(self.id, self.title)


class Offer(models.Model):
    title = models.CharField(max_length=64, verbose_name='Titulo')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Estudiante')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        return "[{}] {}".format(self.id, self.title)


class Contract(models.Model):
    is_accepted_tutor = models.BooleanField(default=False, verbose_name='¿Es aceptado por el tutor?')
    is_accepted_student = models.BooleanField(default=False, verbose_name='¿Es aceptado por el estudiante?')
    price = models.FloatField(default=0, verbose_name='Precio')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.is_accepted_tutor, self.is_accepted_student)


class Aggrement(Contract):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Servicio')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Estudiante')

    class Meta:
        verbose_name = 'Acuerdo'
        verbose_name_plural = 'Acuerdos'


class Nomination(Contract):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, verbose_name='Oferta')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, verbose_name='Tutor')

    class Meta:
        verbose_name = 'Postulacion'
        verbose_name_plural = 'Postulaciones'