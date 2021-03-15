from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import status
from utils.exception import CustomException

from schedules_app.models import Schedule
from users_app.models import Tutor


@receiver(post_save, sender=Tutor)
def registered_tutor(sender, instance, created, **kwargs):
    try:
        if created:
            schedule = Schedule(tutor=instance)
            schedule.save()
    except:
        raise CustomException('No se registro horario al tutor', 'detail', status.HTTP_204_NO_CONTENT)