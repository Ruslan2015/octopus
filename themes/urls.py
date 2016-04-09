from django.conf.urls import url

from . import views



urlpatterns = [
    # ex: /themes/order_number/
    url(r'^', views.index, name='themes'),    
]