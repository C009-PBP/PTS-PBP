from django.urls import path
from homepage.views import *

app_name = 'homepage'

urlpatterns = [
    path('', show_review, name='index'),
    path('json/', show_json, name='show_json'),
    path('add/', add_review, name='add_review'),
    path('add-flutter/', add_review_flutter, name='add_review_flutter'),
    path('delete/<int:id>', delete_review, name='delete_review'),
    path('json-flutter/<int:userId>', show_json_flutter, name='show_json_flutter'),
    path('delete-from-flutter/<int:id>', delete_review_flutter, name='delete_review_flutter'),
]