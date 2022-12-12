from django.urls import path
from pengaturan_akun.views import *

app_name = 'pengaturan_akun'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('med_record/', med_record, name="med_record"),
    path('json/', show_profile_json, name='show_profile_json'),
    path('update/<int:pk>', update_profile_ajax, name='update_profile_ajax'),
    path('update_emergency/<int:pk>', update_emergency_ajax, name='update_emergency_ajax'),
    path('update_record/<int:pk>', update_record_ajax, name='update_record_ajax'),
    path('json-flutter/<int:pk>', show_profile_json_flutter, name='show_profile_json_flutter'),
]