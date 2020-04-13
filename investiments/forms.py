from django.forms import ModelForm
from .models import bc_investiment

class NegotationForm(ModelForm):
    class Meta:
        model = bc_investiment
        fields = ['bc_company_code','amount','total_net_price','average_price','is_active','description']
