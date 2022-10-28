from django.urls import path
from . import views

app_name = 'tanya_dokter'

urlpatterns = [
    path('forum/fill', views.create_forum, name='forum'),
]
