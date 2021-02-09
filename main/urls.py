from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('bbs/', include('bbs.urls')),
    path('account/', include('account.urls'))

]
