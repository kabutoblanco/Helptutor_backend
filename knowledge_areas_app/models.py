from django.db import models

from users_app.models import Tutor, Student, Moderator

# Create your models here.
class KnowledgeArea(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre')
    level = models.IntegerField(default=0, verbose_name='Nivel')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    knowledge_area = models.ManyToManyField('self', blank=True, verbose_name='Especialidades')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Area de conocimiento'
        verbose_name_plural = 'Areas de conocimientos'

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.level, self.name)


class KnowledgeArea_Tutor(models.Model):
    knowledge_area = models.ForeignKey(KnowledgeArea, on_delete=models.CASCADE, verbose_name='Área de conocimiento')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, verbose_name='Tutor')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.knowledge_area, self.tutor)


class KnowledgeArea_Student(models.Model):
    knowledge_area = models.ForeignKey(KnowledgeArea, on_delete=models.CASCADE, verbose_name='Área de conocimiento')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Estudiante')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Interes'
        verbose_name_plural = 'Intereses'

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.knowledge_area, self.student)
 

class Cerficate(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre')
    entity = models.CharField(max_length=64, verbose_name='Entidad')
    issue_year = models.DateField(max_length=64, verbose_name='Año de expedición')
    file = models.FileField(upload_to='certificates', verbose_name='Archivo')
    is_validated = models.BooleanField(default=False, verbose_name='¿Es valido?')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    knowledge_area_tutor = models.ForeignKey(KnowledgeArea_Tutor, on_delete=models.CASCADE, verbose_name='Especialidad tutor')
    moderator = models.ForeignKey(Moderator, on_delete=models.CASCADE, verbose_name='Moderador')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)


class Content(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre')
    file = models.FileField(upload_to='contents', verbose_name='Archivo')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    knowledge_area_tutor = models.ForeignKey(KnowledgeArea_Tutor, on_delete=models.CASCADE, verbose_name='Especialidad tutor')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)
