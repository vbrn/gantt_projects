# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-10 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20180510_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
