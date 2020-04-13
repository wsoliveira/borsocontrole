from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from companies.models import bc_company_code

# Create your models here.
class bc_investiment(models.Model):
    bc_company_code = models.ForeignKey(to='companies.bc_company_code', on_delete=models.PROTECT)
    bc_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    total_net_price = models.DecimalField(max_digits=10, decimal_places=2)
    average_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now, null=True)
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=255, null=True, blank=True, default="")

    def __str__(self):
        return f"{self.bc_company_code.__str__()}-{self.bc_user.__str__()}"

    class Meta:
        verbose_name = 'investiment'
        verbose_name_plural = "investiments"