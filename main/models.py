from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Lists(models.Model):
    
    list_name = models.CharField(max_length=50)
    list_owner = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    list_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Lists"

    def __str__(self):
        return self.list_name

class Tasklist(models.Model):

    task_title = models.CharField(max_length=200)
    task_priority = models.IntegerField(default=5)
    task_due = models.DateTimeField("date task is due", default=datetime.now())
    task_status = models.IntegerField(default=0)
    task_list = models.CharField(max_length=200)
    task_owner = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.task_title

