from django.db import models
from utils.models import HelpTutorModel
from django.utils.translation import ugettext_lazy as _


STATUS_CHOICES = ((0, _("APROVADO")), (1, _("NO APROVADO")), (2, _("EN ESPERA")))

class Payment(HelpTutorModel):
    num_invoice = models.CharField(max_length=64, unique=True, verbose_name='Número de transacción')
    payment = models.FloatField(default=0, verbose_name='Pago')
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    
    contract = models.ForeignKey('services.Contract', on_delete=models.CASCADE, verbose_name='Contrato')

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return "[{}] {}".format(self.id, self.num_invoice)