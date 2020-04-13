from django.db import models
from django.utils import timezone
from administrators.models import bc_admin_type_investiment


# Create your models here.
class bc_sector(models.Model):
    name = models.CharField(max_length=100, unique=True )
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'sector'
        verbose_name_plural = "sectors"

class bc_company(models.Model):
    name = models.CharField(max_length=100)
    identification = models.CharField(max_length=100)
    is_new_market = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now, null=True)
    is_active = models.BooleanField(default=True)
    bc_sector = models.ForeignKey(to=bc_sector, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = "companies"
        ###unique_together = [['name', 'identification']]

class bc_company_code(models.Model):
    name = models.CharField(max_length=50)
    bc_admin_type_investiment = models.ForeignKey(to='administrators.bc_admin_type_investiment', on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now, null=True)
    is_active = models.BooleanField(default=True)
    bc_company = models.ForeignKey(to=bc_company, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'company code'
        verbose_name_plural = "companies codes"
        unique_together = [['name', 'bc_admin_type_investiment']]