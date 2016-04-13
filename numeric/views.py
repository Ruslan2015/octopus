from django.shortcuts import render

# Create your views here.


#from .models import Question


def index(request):
    context = {'test': 'Page Numeric'}
    return render(request, 'numeric/index.html', context)