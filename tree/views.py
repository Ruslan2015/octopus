from django.shortcuts import render
from django.http import HttpResponse

from .models import Tree


def index(request):
    print("index")
    list_all_tree = Tree.objects.get_all_tree()
    current_level = "Корень дерева"
    return render(request, 'tree/index.html', {'list_all_tree': list_all_tree, 'current_level': current_level})

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
    return HttpResponse('{"res" :"'+resstr+'", "test" : "test_item2"}')

def add_love(request):
    return HttpResponse('Добавить в избранное')

def add_node(request):
    return HttpResponse('Добавить узел')

def del_node(request):
    return HttpResponse('Удалить узел')

def level_up(request):
    return HttpResponse('Повысить уровень')

def level_down(request):
    return HttpResponse('Понизить уровень')

def edit_node(request):
    return HttpResponse('Редактировать узел')

def key_up(request):
    return HttpResponse('Переместить выше')

def key_down(request):
    return HttpResponse('Переместить ниже')
