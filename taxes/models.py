from django.db import models
from django.utils import timezone
from negotiations.models import bc_negotiation
from administrators.models import bc_admin_type_negotiation, bc_admin_type_investiment

class bc_tax(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=4)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now, null=True)
    bc_admin_type_negotiation = models.ManyToManyField(to='administrators.bc_admin_type_negotiation')
    bc_admin_type_investiment = models.ManyToManyField(to='administrators.bc_admin_type_investiment', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tax'
        verbose_name_plural = "taxes"

class bc_tax_negotiation(models.Model):
    bc_tax = models.ForeignKey(to=bc_tax, null=True, blank=True, on_delete=models.PROTECT)
    bc_negotiation = models.ForeignKey(to='negotiations.bc_negotiation', null=True, blank=True, on_delete=models.CASCADE)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name = 'tax negotiation'
        verbose_name_plural = "taxes negotiations"
