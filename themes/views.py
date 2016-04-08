from django.shortcuts import render

# Create your views here.
from .models import Themes
#import logging

#logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'mylog.log')

def index(request):
    themes_list = Themes.objects.order_by('number')
    context_dict = {'themes_list': themes_list}
    #logging.info("order_number")
    #logging.info(context_dict)
    return render(request, 'themes/index.html', context_dict)

def order_name(request):
    themes_list = Themes.objects.order_by('name')
    context_dict = {'themes_list': themes_list}
    #logging.info("order_name")
    #logging.info(context_dict)
    return render(request, 'themes/index.html', context_dict)
