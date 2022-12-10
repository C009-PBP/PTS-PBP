from django.urls import path
from info_dokter.views import show_info_dokter
from info_dokter.views import add_review
from info_dokter.views import show_json, show_json2
app_name = 'info_dokter'

urlpatterns = [
    path('', show_info_dokter, name='show_info_dokter'),
    path('add/', add_review, name='add_review'),
    path('json/', show_json, name='show_json'),
    path ('json2/', show_json2, name='show_json2'),
    path('json-flutter/<int:userId>', show_json_flutter, name='show_json_flutter'),
]