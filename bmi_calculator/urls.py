from django.urls import path
from .views import *
# from .views import register, login_user, logout_user

app_name = 'bmi_calculator'

urlpatterns = [
    path('', show_bmi_calculator, name='show_bmi_calculator'),
    path('json/', show_json, name='show_json'),

    path('add/', add_bmi, name='add_bmi'),
    path('add/<int:userPK>', add_bmi_flutter, name='add_bmi_flutter'),
    
    path('delete/<int:id>', delete_bmi, name='delete_bmi'),
    
    path('json-flutter/<int:userPK>', show_json_flutter, name='show_json_flutter'),

    # path('register/', register, name='register'),
    # path('login/', login_user, name='login'),
    # path('logout/', logout_user, name='logout'),
]