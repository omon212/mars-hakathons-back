from django.urls import path
from .views import *

urlpatterns = [
    path('electronic/add/', CreateElectronic.as_view(), name='add_electronic'),
    path('electronic/get/<int:id>/', ElectronicsGetView.as_view(), name='get_electronic'),
    path('report/create/', ReportCreate.as_view(), name='create_report'),
    path('report/delete/', ReportDelete.as_view(), name='delete_report'),
]
