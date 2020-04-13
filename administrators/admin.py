from django.contrib import admin
from .models import bc_admin_type_investiment, bc_admin_type_negotiation

# Register your models here.
admin.site.register(bc_admin_type_investiment)
admin.site.register(bc_admin_type_negotiation)