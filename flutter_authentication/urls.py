from django.urls import path
from .views import *


app_name = 'flutter_authentication'


urlpatterns = [
    path('login/', login, name='login') #?
]