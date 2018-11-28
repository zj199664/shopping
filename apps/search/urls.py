from django.conf.urls import url

from search import views

urlpatterns = [
    url('reslut/', views.search, name='search')

]
