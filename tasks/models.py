from django.db import models

# Create your models here.

class Tasks(models.Model):
    #номер задания
    number = models.CharField(max_length = 6)
    #краткое содержание задания
    context = models.CharField(max_length = 250)
    #требуемый результат
    desired_result = models.CharField(max_length = 250)
    #тема по классификатору
    theme = models.ForeignKey()
    #список рассылки
    list = models.CharField(max_length = 250)
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
    #подразделение заказчика
    dep_employer = models.ForeignKey()
    #заказчик
    employer = models.ForeignKey()
    #подразделение исполнителя
    dep_worker = models.ForeignKey()
    #исполнитель
    worker = models.ForeignKey()
    #ссылка на бланк задания
    href_blank = models.CharField(max_length = 250)
    #ссылка на документ о завершении задания
    href_finished = models.CharField(max_length = 250)
    #список ссылок на результаты задания
    href_results = models.TextField()
    
    
    