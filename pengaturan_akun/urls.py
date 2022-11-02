from django.urls import path
from pengaturan_akun.views import *

app_name = 'pengaturan_akun'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('json/', show_profile_json, name='show_profile_json'),
    path('update/<int:pk>', update_profile_ajax, name='update_profile_ajax'),
]