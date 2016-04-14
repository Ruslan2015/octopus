from django.shortcuts import render

# Create your views here.


#from .models import Question


def index(request):
    context = {'test': 'Page OSHS'}
    return render(request, 'oshs/index.html', context)