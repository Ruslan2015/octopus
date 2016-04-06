from django.conf.urls import url

from . import views

app_name = 'mainpage'

urlpatterns = [
    # ex: /mainpage/
    url(r'^$', views.index, name='index'),
]