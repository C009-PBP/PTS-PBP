from django.urls import path
from .views import *


app_name = 'flutter_authentication'


urlpatterns = [
    path('login/', login, name='login'), #?
    path('logout/', logout, name='logout'),
    path('user-data/', get_user_data, name='get_user_data'), 
    path('register_pasien/', register_pasien, name='register_pasien'),
    path('register_dokter/', register_dokter, name='register_dokter'),

    
]