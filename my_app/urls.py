# C:\Users\TOSHIBA\Desktop\MONAPP_MFS\MFS_APP\my_app\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('changement/', views.changement_view, name='changement'),
    path('incident/', views.incident_view, name='incident'),
    path('inscription/', views.inscription_view, name='inscription'),
    path('login/', views.login_view, name='login'),
]
