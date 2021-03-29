from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
    
    def __str__(self):
        return "[{}] {}".format(self.id, self.user)