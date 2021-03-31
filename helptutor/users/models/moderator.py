"""Moderator model."""


# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Moderator(models.Model):
    """Moderator model.
    
    A moderator is a person in charge of maintaining the
    information of the community within the policies.
    """
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Moderador'
        verbose_name_plural = 'Moderadores'

    def __str__(self):
        return "[{}] {}".format(self.id, self.user)