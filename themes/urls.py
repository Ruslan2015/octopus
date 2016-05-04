from django.conf.urls import url

from . import views



urlpatterns = [
    # ex: /themes/order_number/
    url(r'^index/', views.index, name='themes'),
    url(r'^show_theme_active/', views.show_theme_active, name='show_theme_active'),    
]