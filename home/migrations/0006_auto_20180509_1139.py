# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180508_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name_task',
            field=models.CharField(max_length=30),
        ),
    ]
