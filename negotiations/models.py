from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from companies.models import bc_company_code
from administrators.models import bc_admin_type_investiment, bc_admin_type_negotiation


class bc_negotiation(models.Model):
    bc_admin_type_investiment = models.ForeignKey(to='administrators.bc_admin_type_investiment', on_delete=models.PROTECT)
    bc_admin_type_negotiation = models.ForeignKey(to='administrators.bc_admin_type_negotiation', on_delete=models.PROTECT)
    date_negotiation = models.DateField(null=True, blank=False, default='')
    amount = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    brokerage_price = models.DecimalField(max_digits=10, decimal_places=2)
    gross_total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_net_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, null=True)
    bc_company_code = models.ForeignKey(to='companies.bc_company_code', null=True, blank=True, on_delete=models.PROTECT)
    bc_user = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.bc_company_code.__str__()}-{self.bc_user.__str__()}-{self.bc_admin_type_investiment.__str__()}-{self.bc_admin_type_negotiation.__str__()}"


    class Meta:
        verbose_name = 'negotiation'
        verbose_name_plural = "negotiations"