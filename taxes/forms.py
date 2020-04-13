from django.forms import ModelForm
from .models import bc_tax
from bootstrap_datepicker_plus import DatePickerInput
from administrators.models import bc_admin_type_negotiation, bc_admin_type_investiment

class TaxForm(ModelForm):
    class Meta:
        model = bc_tax
        fields = ['name','value','description','is_active','bc_admin_type_negotiation','bc_admin_type_investiment']

    def __init__(self, *args, **kwargs):
        super(TaxForm, self).__init__(*args, **kwargs)
        self.fields['bc_admin_type_negotiation'].label = 'Types of Negotiation'
        self.fields['bc_admin_type_negotiation'].queryset = bc_admin_type_negotiation.objects.filter(is_active=True)
        self.fields['bc_admin_type_investiment'].label = 'Types of Investiment'
        self.fields['bc_admin_type_investiment'].queryset = bc_admin_type_investiment.objects.filter(is_active=True)