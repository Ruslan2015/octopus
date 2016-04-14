from django.conf.urls import url

from . import views

app_name = 'oshs'

urlpatterns = [
    # ex: oshs/
    url(r'^$', views.index, name='index'),
]