from django.urls import path, include
from .views import negotiation_list, negotiation_new, negotiation_update, negotiation_delete

urlpatterns = [
    path('negotiation/list/', negotiation_list, name='negotiation_list'),
    path('negotiation/new/', negotiation_new, name='negotiation_new'),
    path('negotiation/update/<int:id>/', negotiation_update, name='negotiation_update'),
    path('negotiation/delete/<int:id>/', negotiation_delete, name='negotiation_delete'),
]