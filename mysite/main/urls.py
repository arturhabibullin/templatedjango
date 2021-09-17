from django.urls import path
from .views import *

urlpatterns = [
    path('', samples_list, name='sample_list_url'),
]