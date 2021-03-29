from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tutor(models.Model):    
    score = models.IntegerField(default=0, verbose_name='Puntuación')
    methodology = models.CharField(max_length=120, blank=True, verbose_name='Metodología')
    trajectory = models.CharField(max_length=120, blank=True, verbose_name='Trajectoria')
    skills = models.CharField(max_length=120, blank=True, verbose_name='Habilidades')
    interest = models.CharField(max_length=120, blank=True, verbose_name='Intereses')

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'

    def __str__(self):
        return "[{}] {}".format(self.id, self.user)