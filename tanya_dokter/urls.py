from django.urls import path
from . import views

app_name = 'tanya_dokter'

urlpatterns = [
    # path('forum/fill', views.create_forum, name='forum'),
    path('view/', views.show_landing_page, name='landing_page'),
    path('show/forum/', views.show_forum, name='show_forum'),
    path('add_question/', views.add_question_ajax, name='add_question_ajax'),
]
