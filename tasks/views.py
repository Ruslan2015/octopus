from django.shortcuts import render

# Create your views here.


#from .models import Question


def index(request):
    context = {'test': 'Page Tasks'}
    return render(request, 'tasks/index.html', context)