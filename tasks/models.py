from django.db import models

# Create your models here.

class Tasks(models.Model):
    #����� �������
    number = models.CharField(max_length = 6)
    #������� ���������� �������
    context = models.CharField(max_length = 250)
    #��������� ���������
    desired_result = models.CharField(max_length = 250)
    #���� �� ��������������
    theme = models.ForeignKey()
    #������ ��������
    list = models.CharField(max_length = 250)
    #���� ������ ������
    datatime_order = models.DateTimeField()
    #���� ���������� �� ������������
    datatime_accom = models.DateTimeField()
    #���� ����������� �������
    datatime_approv = models.DateTimeField()
    #��������� ���� ���������� �������
    datatime_deadline = models.DateTimeField()
    #���� ���������� �������
    datatime_finished = models.DateTimeField()
    #������ ������� ���������
    list_number = models.CharField(max_length = 250)
    #������ ������ ����� ������ �� �������
    list_code = models.CharField(max_length = 250)
    #������������� ���������
    dep_employer = models.ForeignKey()
    #��������
    employer = models.ForeignKey()
    #������������� �����������
    dep_worker = models.ForeignKey()
    #�����������
    worker = models.ForeignKey()
    #������ �� ����� �������
    href_blank = models.CharField(max_length = 250)
    #������ �� �������� � ���������� �������
    href_finished = models.CharField(max_length = 250)
    #������ ������ �� ���������� �������
    href_results = models.TextField()
    
    
    