from django.conf.urls import url

from . import views

app_name = 'tree'

urlpatterns = [
    # ex: oshs/
    url(r'^index/', views.index, name='index'),
    url(r'^show_node_context/$', views.show_node_context, name='show_node_context'),
]