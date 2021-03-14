from django.db import models
from django.contrib.auth.models import Permission, AbstractUser
from django.utils.translation import ugettext_lazy as _

from places_app.models import City, University

# Create your models here.
GENDER_CHOICES = ((0, _("MUJER")), (1, _("HOMBRE")), (2, _("NA")))

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, verbose_name='Correo')
    photo = models.FileField(upload_to='profiles/photos', null= True, verbose_name='Foto')
    telephone = models.CharField(max_length=64,blank = True, verbose_name='Telefono')
    gender = models.IntegerField(default=0, choices=GENDER_CHOICES, verbose_name='Genero')
    is_verified = models.BooleanField(default=False, verbose_name='¿Es verificado?')
    is_completed = models.BooleanField(default=False, verbose_name='¿Es completo?')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Universidad')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Ciudad')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Tutor(User):
    score = models.IntegerField(default=0, verbose_name='Puntuación')
    methodology = models.CharField(max_length=120, blank = True,verbose_name='Metodología')
    trajectory = models.CharField(max_length=120,blank = True, verbose_name='Trajectoria')
    skills = models.CharField(max_length=120,blank = True, verbose_name='Habilidades')
    interest = models.CharField(max_length=120,blank = True, verbose_name='Intereses')

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'


class Student(User):

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'


class Moderator(User):

    class Meta:
        verbose_name = 'Moderador'
        verbose_name_plural = 'Moderador'
