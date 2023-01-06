from django.contrib import admin
from .models import *
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','complete','date_created']

admin.site.register(Task,TaskAdmin)