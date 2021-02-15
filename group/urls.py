from django.urls import path
from . import views

app_name = 'group'


urlpatterns = [

    path('group_main/', views.group_main, name="group_main"),


]
