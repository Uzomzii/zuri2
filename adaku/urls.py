from django.urls import path 
from .views import homepage, get_name


urlpatterns = [ path('', homepage, name='home'),
path('forms/', get_name, name='form'),
]