from django.db import models
from django.utils.translation import ugettext_lazy as _


class Moderator(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Moderador'
        verbose_name_plural = 'Moderadores'

    def __str__(self):
        return "[{}] {}".format(self.id, self.user)