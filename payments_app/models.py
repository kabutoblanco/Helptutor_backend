from django.db import models
from django.utils.translation import ugettext_lazy as _

from services_app.models import Contract

# Create your models here.
STATUS_CHOICES = ((0, _("APROVADO")), (1, _("NO APROVADO")), (2, _("EN ESPERA")))

class Payment(models.Model):
    num_invoice = models.CharField(max_length=64, unique=True, verbose_name='Número de transacción')
    payment = models.FloatField(default=0, verbose_name='Pago')
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='Contrato')

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return "[{}] {}".format(self.id, self.num_invoice)