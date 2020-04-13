from django.db import models
from django.utils import timezone

# Create your models here.
class bc_admin_type_investiment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'admin type investiment'
        verbose_name_plural = "admin types investiments"

class bc_admin_type_negotiation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'admin type negotiation'
        verbose_name_plural = "admin types negotiations"