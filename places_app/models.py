from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre')
    cod = models.CharField(max_length=2, verbose_name='Código')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)


class State(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre')
    cod = models.CharField(max_length=3, verbose_name='Código')

    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='País')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)


class City(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre')

    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Departamento')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)


class University(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre')

    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Ciudad')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)