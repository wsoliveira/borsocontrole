from django import forms
#from django.forms import ModelForm
from .models import bc_negotiation
from bootstrap_datepicker_plus import DatePickerInput
from administrators.models import bc_admin_type_investiment, bc_admin_type_negotiation
from companies.models import bc_company_code

#https://pt.stackoverflow.com/questions/420444/formul%C3%A1rio-modelform-din%C3%A2mico-django
#https://stackoverflow.com/questions/42820728/filter-a-django-form-select-element-based-on-a-previously-selected-element
#https://dev.to/zxenia/django-inline-formsets-with-class-based-views-and-crispy-forms-14o6
#https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html

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
        self.fields['bc_company_code'].queryset = bc_company_code.objects.none()

        if 'bc_admin_type_investiment' in self.data:
            try:
                bc_admin_type_investiment_id = int(self.data.get('bc_admin_type_investiment'))
                self.fields['bc_company_code'].queryset = bc_company_code.objects.filter(bc_admin_type_investiment=bc_admin_type_investiment_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty bc_company_code queryset
        elif self.instance.pk:
            self.fields['bc_company_code'].queryset = self.instance.bc_admin_type_investiment.bc_company_code_set.order_by('name')
