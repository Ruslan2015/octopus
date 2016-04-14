from django.contrib import admin

# Register your models here.

from oshs.models import Enterprise, MacroDepartment, Department, SubDepartment, UserProfile

admin.site.register(Enterprise)
admin.site.register(MacroDepartment)
admin.site.register(Department)
admin.site.register(SubDepartment)
admin.site.register(UserProfile)
