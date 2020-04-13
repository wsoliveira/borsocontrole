from django.contrib import admin
from .models import bc_tax, bc_tax_negotiation

# Register your models here.
admin.site.register(bc_tax)
admin.site.register(bc_tax_negotiation)