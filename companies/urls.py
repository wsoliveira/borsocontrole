from django.urls import path, include
from .views import sector_list, sector_new, sector_update, sector_delete, company_list,\
    company_new, company_update, company_delete, company_code_delete, company_code_list, company_code_new, company_code_update

urlpatterns = [
    path('sector/list/', sector_list, name='sector_list'),
    path('sector/new/', sector_new, name='sector_new'),
    path('sector/update/<int:id>/', sector_update, name='sector_update'),
    path('sector/delete/<int:id>/', sector_delete, name='sector_delete'),
    path('company/list/', company_list, name='company_list'),
    path('company/new/', company_new, name='company_new'),
    path('company/update/<int:id>/', company_update, name='company_update'),
    path('company/delete/<int:id>/', company_delete, name='company_delete'),
    path('company_code/list/', company_code_list, name='company_code_list'),
    path('company_code/new/', company_code_new, name='company_code_new'),
    path('company_code/update/<int:id>/', company_code_update, name='company_code_update'),
    path('company_code/delete/<int:id>/', company_code_delete, name='company_code_delete'),
]