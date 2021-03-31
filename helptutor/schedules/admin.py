from django.contrib import admin

from helptutor.schedules.models.schedule import *
from helptutor.schedules.models.time_slot import *

# Register your models here.
admin.site.register([Schedule, TimeSlot, ])