# Generated by Django 3.0.4 on 2020-04-17 18:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200417_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='task_due',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 17, 23, 38, 1, 600339), verbose_name='date task is due'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='task_list',
            field=models.CharField(max_length=200),
        ),
    ]
