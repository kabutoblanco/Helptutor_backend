from django.contrib.auth.models import Permission, AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import HelpTutorModel

from .tutor import Tutor

# Create your models here.
GENDER_CHOICES = ((0, _("MUJER")), (1, _("HOMBRE")), (2, _("NA")))

class User(HelpTutorModel, AbstractUser):
    email = models.EmailField(max_length=254, unique=True, verbose_name='Correo')
    photo = models.FileField(upload_to='profiles/photos', null=True, default='', verbose_name='Foto')
    telephone = models.CharField(max_length=64, blank=True, verbose_name='Telefono')
    gender = models.IntegerField(default=2, choices=GENDER_CHOICES, verbose_name='Genero')
    birthday = models.DateField(null=True, blank=True, verbose_name='Cumpleaños')
    is_verified = models.BooleanField(default=False, verbose_name='¿Es verificado?')
    is_completed = models.BooleanField(default=False, verbose_name='¿Es completo?')
    description = models.CharField(max_length=120, blank=True, verbose_name='Descripción')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    university = models.ForeignKey('places.University', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Universidad')
    city = models.ForeignKey('places.City', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Ciudad')

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    

    def is_tutor(self, *args, **kwargs):
        try:
            tutor = Tutor.objects.get(user=self)
            if tutor:
                return True
        except Tutor.DoesNotExist:
            return False

    def is_student(self, *args, **kwargs):
        pass

    def is_moderator(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return "[{}] {}".format(self.id, self.email)