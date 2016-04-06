from django.conf.urls import url

from . import views

app_name = 'tasks'

urlpatterns = [
    # ex: /mainpage/
    url(r'^$', views.index, name='index'),
]