from django.conf.urls import url

from apps.detail import views

urlpatterns = [
    url('detail/', views.detail, name='detail')
]
