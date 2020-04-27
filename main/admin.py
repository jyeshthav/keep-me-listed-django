from django.contrib import admin
from .models import Tasklist, Lists
# from .models import Owner
from tinymce import TinyMCE
from django.db import models

class TasklistAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Task/date', {'fields': ['task_title', 'task_due']}),
        ('Description', {'fields': ['task_priority']}),
        ('List', {'fields': ['task_list']}),
        ('Owner', {'fields': ['task_owner']}),
    ]
    
    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE()}
    }



# Register your models here.
# admin.site.register(Owner)
admin.site.register(Lists)
admin.site.register(Tasklist)