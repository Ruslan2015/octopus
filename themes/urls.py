from django.conf.urls import url

from . import views



urlpatterns = [
    # ex: /themes/
    url(r'^', views.index, name='themes'),
    # ex: /themes/order_number/
    url(r'^order_number/', views.index, name='themes_order_number'),
    # ex: /themes/order_name/
    url(r'^order_name/', views.order_name, name ='themes_order_name'),
]