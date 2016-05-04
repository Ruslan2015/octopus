from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import FilterThemes
from django.http import HttpResponse

# Create your views here.
from .models import Themes
#import logging

#logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'mylog.log')

def index(request):
    #Если страница вызвана через POST
    if request.method == 'POST':
        form = FilterThemes(request.POST)
        if form.is_valid():
            themes_list = Themes.objects.filter(name__contains=form.cleaned_data['name'])
        else:
            themes_list = Themes.objects.order_by('number')
    #Если страница вызвана через GET    
    else:
        form = FilterThemes()
        themes_list = Themes.objects.order_by('number')
    
    paginator = Paginator(themes_list, 20)
    
    page = request.GET.get('page')
    
    try:
        themes = paginator.page(page)
    except PageNotAnInteger:
        themes = paginator.page(1)
    except EmptyPage:
        themes = paginator.page(paginator.num_pages)
    
    
#     return render_to_response('themes/index.html', {'form': form, 'themes': themes})
    return render(request, 'themes/index.html', {'form': form, 'themes': themes})
   
def show_theme_active(request):

    print("Show_theme_active")
    theme_id = None
    if request.method == 'GET':
        theme_id = request.GET['theme_id']
        request.session['theme_id'] = theme_id    
    theme_active = Themes.objects.show_active(theme_id)
    print(str(theme_active[0].id))
    resnum = request.session.get('theme_id')    
    return HttpResponse('{"resnum" :"'+resnum+'", "resname" : "'+str(theme_active[0].name)+'"}')
