from django.conf.urls import url

from . import views

app_name = 'themes'

urlpatterns = [
    # ex: /themes/
    url(r'^$', views.index),
]