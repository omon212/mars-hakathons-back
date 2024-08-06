from django.urls import path
from .views import *

urlpatterns = [
    path('electroncs/add', CreateElectronic.as_view(), name='add_electronic'),
]
