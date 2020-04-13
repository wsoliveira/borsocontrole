from django import forms
#from django.forms import ModelForm
from .models import bc_negotiation
from bootstrap_datepicker_plus import DatePickerInput
from administrators.models import bc_admin_type_investiment, bc_admin_type_negotiation

#https://pt.stackoverflow.com/questions/420444/formul%C3%A1rio-modelform-din%C3%A2mico-django

class NegotationForm(forms.ModelForm):
    class Meta:
        model = bc_negotiation
        fields = [
            'bc_admin_type_negotiation','bc_admin_type_investiment','bc_company_code','date_negotiation','amount',
            'unit_price','brokerage_price','description'
        ]
        widgets = {
            'date_negotiation': DatePickerInput(format='%Y-%m-%d'), # default date-format %m/%d/%Y will be used
        }

    def clean_amount(self):
        data = self.cleaned_data.get("amount")
        if int(data) < 1:
            raise forms.ValidationError("Ops ! Must be greater than 0 (zero) !")
        return data

    def __init__(self, *args, **kwargs):
        super(NegotationForm, self).__init__(*args, **kwargs)
        self.fields['bc_admin_type_investiment'].label = 'Type of Investiment'
        self.fields['bc_admin_type_negotiation'].label = 'Type of Negotiation'
        self.fields['bc_company_code'].label = 'Company Code'
        self.fields['bc_admin_type_investiment'].queryset = bc_admin_type_investiment.objects.filter(is_active=True)
        self.fields['bc_admin_type_negotiation'].queryset = bc_admin_type_negotiation.objects.filter(is_active=True)
