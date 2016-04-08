from django.shortcuts import render

# Create your views here.
from .models import Themes


def index(request):
    themes_list = Themes.objects.order_by('number')
    context_dict = {'themes_list': themes_list}
    return render(request, 'themes/index.html', context_dict)

def order_name(request):
    themes_list = Themes.objects.order_by('-name')
    context_dict = {'themes_list': themes_list}
    return render(request, 'themes/index.html', context_dict)
