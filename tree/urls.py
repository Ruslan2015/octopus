from django.conf.urls import url

from . import views

app_name = 'tree'

urlpatterns = [
    # ex: oshs/
    url(r'^index/', views.index, name='index'),
    url(r'^show_node_context/$', views.show_node_context, name='show_node_context'),
    url(r'^add_love/', views.add_love, name='add_love'),
    url(r'^add_node/', views.add_node, name='add_node'),
    url(r'^del_node/', views.del_node, name='del_node'),
    url(r'^level_up/', views.level_up, name='level_up'),
    url(r'^level_down/', views.level_down, name='level_down'),
    url(r'^edit_node/', views.edit_node, name='edit_node'),
    url(r'^key_up/', views.key_up, name='key_up'),
    url(r'^key_down/', views.key_down, name='key_down'),
]