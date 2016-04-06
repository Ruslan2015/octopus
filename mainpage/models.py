from django.db import models

# Create your models here.

#������� ������� �� ������������
class MpCoordTask(models.Model):
    #����� �������
    number = models.CharField(max_length = 10)
    #������� ��������
    description = models.TextField()
    #���� �������������
    pubdate = models.DateTimeField()
    #������ �����������
    listworkers = models.TextField()
    
#������� ������������� �� ������� ������
class MpDeadlineTask(models.Model):
    #����� �������
    number = models.CharField(max_length = 10)
    #������� �������� �������
    description = models.TextField()
    #���� ����������
    deadline = models.DateTimeField()
    #�����������
    worker = models.CharField(max_length = 250)
    
#������� ������������� �� ������ �����
class MpDeadlineWorks(models.Model):
    #����� ������
    number = models.CharField(max_length = 10)
    #������
    project = models.CharField(max_length = 250)
    #������� ��������
    description = models.TextField()
    #����
    daedline = models.DateTimeField()
    #�����������
    worker = models.CharField(max_length = 250)
    

    