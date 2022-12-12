from django.urls import path
from . import views

app_name = 'tanya_dokter'

urlpatterns = [
    # path('forum/fill', views.create_forum, name='forum'),
    path('', views.show_landing_page, name='landing_page'),
    path('forum/', views.home, name='home'),
    path('forum/detail/<int:id>/', views.show_detail, name='detail'),
    path('save-comment/', views.save_comment, name='save-comment'),
    path('add_question/', views.ask_form, name='ask-question'),
    path('json/<int:id>/', views.form_ajax, name='form_ajax'),
    path('json-all/<int:id>/', views.home_flutter, name='home_flutter'),
    # path('view/', views.ForumView.as_view(), name='forum_view'),
    # path('create/forum', views.CreateForum.as_view(), name='create_forum'),
    
]
