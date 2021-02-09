from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('bbs/', include('bbs.urls')),
    path('account/', include('account.urls'))

]
