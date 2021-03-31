from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import status
from utils.error import ValidationError

from helptutor.schedules.models import Schedule
from helptutor.users.models import Tutor


@receiver(post_save, sender=Tutor)
def registered_tutor(sender, instance, created, **kwargs):
    try:
        if created:
            schedule = Schedule(tutor=instance)
            schedule.save()
    except:
        raise ValidationError('No se registro horario al tutor')