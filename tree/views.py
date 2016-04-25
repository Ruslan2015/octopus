from django.shortcuts import render
from django.http import HttpResponse

from .models import Tree

# Create your views here.

def index(request):
    print("index")
    list_all_tree = Tree.objects.get_all_tree()
    return render(request, 'tree/index.html', {'list_all_tree': list_all_tree})

def show_node_context(request):

    print("Show_node_context")
    node_id = None
    if request.method == 'GET':
        node_id = request.GET['node_id']
        request.session['node_id'] = node_id
    node = Tree.objects.filter(id=node_id)
    print(node)
    resstr = 'Уровень: '+str(node[0].level)+'Left_key: '+str(node[0].left_key)+'Right_key: '+str(node[0].right_key)
    resstr = resstr + 'куки: node_id---' + request.session.get('node_id')
    return HttpResponse(resstr)
