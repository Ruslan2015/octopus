from django.db import models
from django.db.models import F

# Create your models here.

class TreeManager(models.Manager):

    def create_root(self):
        # Удаляем все записи
        res_del = self.all().delete()
        # Создаем корневой элемент 
        result = self.create(name = 'root', level = 1, left_key = 1,
                                     right_key = 2)
        
    def show_tree(self):
        result = self.all()        
        return result

    def get_all_tree(self):
        res_qs = self.order_by('left_key')
        res = '<ul class="ul-treefree ul-dropfree">'
        inline = 0
        for rec in res_qs:
            #Проверяем, есть ли потомки
            if((rec.right_key - rec.left_key) == 1):
                btn = '<button class="tree_node" data-catid="'+str(rec.id)+'" type="button">'+str(rec.id)+'</button>'
                res = res + '<li>' + btn + '</li>'
                if(inline != 0):
                    res = res + '</ul>'
                    inline = inline - 1
            else:
                btn = '<button class="tree_node" data-catid="'+str(rec.id)+'" type="button">'+str(rec.id)+'</button>'
                res = res + '<li>' + btn + '<ul>'
                inline = inline +1
        res = res + '</ul>'
        return res

    def add_node(self, parent_level, parent_right_key):
        # Обновляем ключи существующего дерева,
        # узлы стоящие за родительским узлом
        # UPDATE my_tree SET left_key = left_key + 2, right_ key = right_ key +2
        # WHERE left_key > $right_ key
        if(parent_level != 0):            
            resbottom = self.filter(left_key__gt=parent_right_key
                                 ).update(left_key=F('left_key')+2,
                                          right_key=F('right_key')+2)
            print("Обновлено вниз и вправо: ", resbottom)
            # Обновляем родительскую ветку:
            # UPDATE my_tree SET right_key = right_key + 2
            # WHERE right_key >= $right_key
            # AND left_key < $right_key        
            restop = self.filter(right_key__gte=parent_right_key,
                                 left_key__lt=parent_right_key).update(
                                     right_key=F('right_key')+2)
            print("Обновлено вверх: ", restop)
                    
            # Теперь добавляем новый узел :
            # INSERT INTO my_tree SET left_key = $right_key,
            # right_key = $right_key + 1, level = $level + 1
            resadd = self.create(left_key = parent_right_key,
                           right_key = parent_right_key + 1,
                           level = parent_level + 1)
            print("Узел добавлен", resadd)

        if(parent_level == 0):
            resadd = self.create(left_key = parent_right_key + 1,
                           right_key = parent_right_key + 2,
                           level = parent_level + 1)
            print("Узел добавлен", resadd)
        return True

       
class Tree(models.Model):
    name = models.CharField(max_length = 150)
    left_key = models.IntegerField()
    right_key = models.IntegerField()
    level = models.IntegerField()
    objects = TreeManager()

    def __str__(self):
        str_1 = str(self.id)+"/"+str(self.level)+"/"+str(self.left_key)+"/"+str(self.right_key)
        return str_1

    
    
        

            
