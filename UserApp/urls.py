from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Register.as_view(), name='Register API'),
    path('login/', Login.as_view(), name='Login API'),
]
