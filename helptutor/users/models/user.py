"""User model."""


# Django
from django.contrib.auth.models import Permission, AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# models
from .tutor import Tutor

# Utilities
from utils.models import HelpTutorModel


GENDER_CHOICES = ((0, _("MUJER")), (1, _("HOMBRE")), (2, _("NA")))

class User(HelpTutorModel, AbstractUser):
    """User model."""
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

    def __str__(self):
        return "[{}] {}".format(self.id, self.email)