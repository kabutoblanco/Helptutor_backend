from django.db import models

from utils.models import HelpTutorModel


class Chat(HelpTutorModel):
    log = models.FileField(upload_to='chats', verbose_name='Log')

    sesion = models.ForeignKey('sesions.Sesion', on_delete=models.CASCADE, verbose_name='Sesión')

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

    def __str__(self):
        return "[{}] {}".format(self.id, self.sesion)