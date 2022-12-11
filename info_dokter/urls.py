from django.urls import path
from info_dokter.views import *
from info_dokter.views import show_info_dokter
from info_dokter.views import add_review
from info_dokter.views import show_json, show_json2
from info_dokter.views import show_json_flutter
from info_dokter.views import add_review_flutter

app_name = 'info_dokter'

urlpatterns = [
    path('', show_info_dokter, name='show_info_dokter'),
    path('add/<int:userId>', add_review_flutter, name='add_review_flutter'),
    path('json/', show_json, name='show_json'),
    path ('json2/', show_json2, name='show_json2'),
    path('json-flutter/<int:userId>', show_json_flutter, name='show_json_flutter'),
]
