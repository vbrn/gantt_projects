# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-04 12:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20180604_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='promizhny_date',
            field=models.DateField(default=datetime.date(1, 1, 1), verbose_name='Не на контролi'),
        ),
    ]
