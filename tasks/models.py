from django.db import models
from django.contrib.auth.models import User
 
from themes.models import Themes
# Create your models here.

class Tasks(models.Model):
    #номер задания
    number = models.CharField(max_length = 6)
    #краткое содержание задания
    context = models.CharField(max_length = 250)
    #требуемый результат
    desired_result = models.CharField(max_length = 250)
    #тема по классификатору
    theme = models.ForeignKey(Themes)
    #список рассылки
    netlist = models.CharField(max_length = 250)
    #дата подачи заявки
    datatime_order = models.DateTimeField()
    #дата публикации на согласование
    datatime_accom = models.DateTimeField()
    #дата утверждения задания
    datatime_approv = models.DateTimeField()
    #требуемый срок завершения задания
    datatime_deadline = models.DateTimeField()
    #дата завершения задания
    datatime_finished = models.DateTimeField()
    #список номеров агрегатов
    list_number = models.CharField(max_length = 250)
    #список шифров учета затрат по заданию
    list_code = models.CharField(max_length = 250)
    #заказчик
    employer = models.ForeignKey(User, on_delete = models.CASCADE, related_name='employer')
    #исполнитель
    worker = models.ForeignKey(User, on_delete = models.CASCADE, related_name='worker')
    #ссылка на бланк задания
    href_blank = models.CharField(max_length = 250)
    #ссылка на документ о завершении задания
    href_finished = models.CharField(max_length = 250)
    #список ссылок на результаты задания
    href_results = models.TextField()
    #если нужно ОТК
    needed_otk = models.BooleanField()
    #если нужно ВП
    needed_vp = models.BooleanField()
    
    def __str__(self):
        retstr = self.number + '-' + self.context
        return retstr
    
