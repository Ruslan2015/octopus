from django.conf.urls import url

from . import views

app_name = 'numeric'

urlpatterns = [
    # ex: numeric/
    url(r'^$', views.index, name='index'),
]