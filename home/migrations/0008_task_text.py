# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-10 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='text',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
