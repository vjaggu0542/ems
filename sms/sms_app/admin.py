from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class Usermodel(UserAdmin):
    list_display=['username','user_type']

admin.site.register(Customuser,Usermodel)
admin.site.register(Designation)
admin.site.register(Duration)
admin.site.register(Employee)
admin.site.register(Teamlead)


