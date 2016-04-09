from django.db import models

# Create your models here.

class Themes(models.Model):
    number = models.CharField(max_length = 10)
    name = models.CharField(max_length = 50)
    specification = models.CharField(max_length = 100)
    status = models.CharField(max_length = 50)
    
    def __str__(self):      # Используйте __unicode в Python 2 и __str__ в Python 3
        return (self.number + "-" + self.name)
