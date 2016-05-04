from django.db import models

class ThemesManager(models.Manager):

    def show_active(self, theme_id):
        theme_active = Themes.objects.filter(id=theme_id)
        return theme_active

class Themes(models.Model):
    number = models.CharField(max_length = 10)
    name = models.CharField(max_length = 50)
    specification = models.CharField(max_length = 100)
    status = models.CharField(max_length = 50)
    objects = ThemesManager()
    
    def __str__(self):      # Используйте __unicode в Python 2 и __str__ в Python 3
        return (self.number + "-" + self.name)
