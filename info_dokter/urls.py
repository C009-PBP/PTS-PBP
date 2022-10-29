from django.urls import path
from info_dokter.views import show_info_dokter
from info_dokter.views import add_review
from info_dokter.views import show_json
app_name = 'info_dokter'

urlpatterns = [
    path('', show_info_dokter, name='show_info_dokter'),
    path('add/', add_review, name='add_review'),
    path('json/', show_json, name='show_json'),
]