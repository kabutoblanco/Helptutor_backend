from django.db import models

from users_app.models import User, Student

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=64, verbose_name='Titulo')
    description = models.CharField(max_length=120, verbose_name='Descripción')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Estudiante')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'

    def __str__(self):
        return "[{}] {}".format(self.id, self.title)


class Answer(models.Model):
    description = models.CharField(max_length=120, verbose_name='Descripción')

    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, verbose_name='Anuncio')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return "[{}]".format(self.id)