from django.urls import path, include
from .views import investiment_list, investiment_delete

urlpatterns = [
    path('investiment/list/', investiment_list, name='investiment_list'),
    path('investiment/delete/<int:id>/', investiment_delete, name='investiment_delete'),
]