from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('main/', views.main, name='main'),
]
