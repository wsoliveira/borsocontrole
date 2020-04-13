from django.urls import path, include
from .views import tax_list, tax_new, tax_update, tax_delete, tax_negotiation_list

urlpatterns = [
    path('tax/list/', tax_list, name='tax_list'),
    path('tax/new/', tax_new, name='tax_new'),
    path('tax/update/<int:id>/', tax_update, name='tax_update'),
    path('tax/delete/<int:id>/', tax_delete, name='tax_delete'),
    path('tax_negotiation/list/<int:id_negotiation>/', tax_negotiation_list, name='tax_negotiation_list'),
]