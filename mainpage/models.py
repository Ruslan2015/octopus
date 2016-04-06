from django.db import models

# Create your models here.

#Таблица заданий на согласовании
class MpCoordTask(models.Model):
    #Номер задания
    number = models.CharField(max_length = 10)
    #Краткое описание
    description = models.TextField()
    #Дата опубликования
    pubdate = models.DateTimeField()
    #Список согласующих
    listworkers = models.TextField()
    
#Таблица завершающихся на текущей неделе
class MpDeadlineTask(models.Model):
    #Номер задания
    number = models.CharField(max_length = 10)
    #Краткое описание задания
    description = models.TextField()
    #Срок исполнения
    deadline = models.DateTimeField()
    #Исполнитель
    worker = models.CharField(max_length = 250)
    
#Таблица завершающихся на неделе работ
class MpDeadlineWorks(models.Model):
    #Номер работы
    number = models.CharField(max_length = 10)
    #Проект
    project = models.CharField(max_length = 250)
    #Краткое описание
    description = models.TextField()
    #Срок
    daedline = models.DateTimeField()
    #Исполнитель
    worker = models.CharField(max_length = 250)
    

    