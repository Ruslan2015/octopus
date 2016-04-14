from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Enterprise(models.Model):
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name


class MacroDepartment(models.Model):
    inbox = models.ForeignKey(Enterprise)
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name


class Department(models.Model):
    inbox = models.ForeignKey(MacroDepartment)
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name


class SubDepartment(models.Model):
    inbox = models.ForeignKey(Department)
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    #Эта строка обязательна. Связывает с экземпляром модели User
    user = models.OneToOneField(User)
    #Дополнительные атрибуты, которые мы добавляем
    indep = models.ForeignKey(Department)

    def __str__(self):
        return self.user.username

    
    
