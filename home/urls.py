from django.urls import path, include
from .views import home
from investiments.views import investiment_list

urlpatterns = [
    path('', investiment_list, name='home'),
]