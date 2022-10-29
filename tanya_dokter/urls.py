from django.urls import path
from . import views

app_name = 'tanya_dokter'

urlpatterns = [
    # path('forum/fill', views.create_forum, name='forum'),
    path('', views.show_landing_page, name='landing_page'),
    path('show/forum/', views.show_forum, name='show_forum'),
    path('add_question/', views.add_question_ajax, name='add_question_ajax'),
    path('json/', views.form_ajax, name='form_ajax'),
    # path('view/', views.ForumView.as_view(), name='forum_view'),
    # path('create/forum', views.CreateForum.as_view(), name='create_forum'),
    
]
