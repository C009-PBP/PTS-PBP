from django.urls import path
from .views import *


app_name = 'flutter_authentication'


urlpatterns = [
    path('login/', login, name='login'), #?
    path('logout/', logout, name='logout'),
    path('user-data/', get_user_data, name='get_user_data'), 
]