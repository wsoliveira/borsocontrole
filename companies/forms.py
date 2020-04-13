from django.forms import ModelForm
from .models import bc_sector, bc_company, bc_company_code
from administrators.models import bc_admin_type_investiment

class SectorForm(ModelForm):
    class Meta:
        model = bc_sector
        fields = ['name','description','is_active']


class CompanyForm(ModelForm):
    class Meta:
        model = bc_company
        fields = ['name','identification','is_new_market','bc_sector']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['bc_sector'].label = 'Sector'
        self.fields['bc_sector'].queryset = bc_sector.objects.filter(is_active=True)


class CompanyCodeForm(ModelForm):
    class Meta:
        model = bc_company_code
        fields = ['name','bc_admin_type_investiment','bc_company']

    def __init__(self, *args, **kwargs):
        super(CompanyCodeForm, self).__init__(*args, **kwargs)
        self.fields['bc_admin_type_investiment'].label = 'Type of Investiment'
        self.fields['bc_admin_type_investiment'].queryset = bc_admin_type_investiment.objects.filter(is_active=True)
        self.fields['bc_company'].label = 'Company'
        self.fields['bc_company'].queryset = bc_company.objects.filter(is_active=True)