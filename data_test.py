import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from themes.models import Themes


def populate():    

    add_themes(number = '001',
        name="ДТ-117",
        specification = "ТУ 100.700.001.123",
        status = "НИОКР")
    
    add_themes(number = '002',
        name="ДТФ-117",
        specification = "ТУ 100.600.001.123",
        status = "НИОКР")
    
    add_themes(number = '003',
        name="АГ-117",
        specification = "ТУ 100.500.001.123",
        status = "НИОКР")
    
    add_themes(number = '004',
        name="АУПН-117",
        specification = "ТУ 100.400.001.123",
        status = "НИОКР")
    
    for i in range(100):
        add_themes(number = str(i),
            name="АУПН-117",
            specification = "ТУ 100.400.001.123",
            status = "НИОКР")


def add_themes(number, name, specification, status):
    th = Themes.objects.get_or_create(number=number, name=name, specification=specification, status=status)[0]
    th.save()
    return th



# Код начинает выполняться отсюда!
if __name__ == '__main__':
    print("Starting fulling datatest for db...")
    populate()
    print("Finished fulling datatest for db...")