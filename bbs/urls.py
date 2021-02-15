from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('logout/', views.logout, name='logout'),
    path('board/', views.board, name='board'),
    path('board/<int:post_id>/', views.detail, name='detail'),
    path('board/register/', views.post_register, name='post_register')
]
