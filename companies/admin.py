from django.contrib import admin
from .models import bc_company, bc_company_code, bc_sector

# Register your models here.
admin.site.register(bc_company)
admin.site.register(bc_company_code)
admin.site.register(bc_sector)