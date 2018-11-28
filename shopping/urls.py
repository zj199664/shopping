from django.conf.urls import url, include
from django.contrib import admin

from apps.main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', views.index, name='index'),
    url('main/', include('apps.main.urls')),
    url('shop/', include('apps.detail.urls')),
    url('search/', include('apps.search.urls')),
    url('account/', include('apps.account.urls')),
]
