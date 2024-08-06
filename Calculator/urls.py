from django.urls import path
from .views import *

urlpatterns = [
    path('electronics/add/', CreateElectronic.as_view(), name='add_electronic'),
    path('report/create/', ReportCreate.as_view(), name='create_report'),
    path('report/delete/', ReportDelete.as_view(), name='delete_report'),
]
