from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register([KnowledgeArea, KnowledgeArea_Tutor, KnowledgeArea_Student, Cerficate, Content, ])