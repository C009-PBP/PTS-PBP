from django.urls import path
from homepage.views import show_review, show_json, add_review, delete_review

app_name = 'homepage'

urlpatterns = [
    path('', show_review, name='index'),
    path('json/', show_json, name='show_json'),
    path('add/', add_review, name='add_review'),
    path('delete/<int:id>', delete_review, name='delete_review'),
]