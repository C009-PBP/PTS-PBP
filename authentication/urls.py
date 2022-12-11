from django.urls import path
from authentication.views import register, register_pasien, register_dokter, login_user, logout_user
from .pasien import PasienSignUpView
from .dokter import DokterSignUpView

from .views import *


app_name = 'authentication'

urlpatterns =[
    path('register/', register, name='register'),
    path('register/pasien/', PasienSignUpView.as_view(), name='register_pasien'),
    path('register/dokter/', DokterSignUpView.as_view(), name='register_dokter'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user-json/<int:userPK>', get_user_json, name='get_user_json'),

]