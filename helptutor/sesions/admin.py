from django.contrib import admin

from helptutor.sesions.models.sesion import *
from helptutor.sesions.models.classroom import *
from helptutor.sesions.models.chat import *
from helptutor.sesions.models.qualification import *

# Register your models here.
admin.site.register([Sesion, Classroom, Chat, Qualification, ])