# Generated by Django 3.0.4 on 2020-04-17 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200417_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='task_due',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 17, 23, 40, 26, 991358), verbose_name='date task is due'),
        ),
    ]