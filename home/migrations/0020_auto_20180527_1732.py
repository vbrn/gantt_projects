# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-27 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20180520_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='CONTROL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_admin', models.CharField(help_text="Введіть ім'я, кому посилати звіт (система буде к ньйому звертатися)", max_length=50, verbose_name="Ім'я")),
                ('email', models.EmailField(help_text='введіть е-мейл, которому нужно посилати звіт', max_length=254, verbose_name='Електронна Пошта')),
                ('status', models.CharField(choices=[('d', 'Кожний день'), ('w', 'Раз на тиждень'), ('m', 'Раз на місяць'), ('n', 'Не посилати мені звіт')], default='n', max_length=1, verbose_name='Коли вам посилати звіт')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='overdue',
            field=models.BooleanField(default=True, verbose_name='Не прострочена'),
        ),
        migrations.AlterField(
            model_name='task',
            name='promizhny',
            field=models.BooleanField(default=True, verbose_name='Не на контролi'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('n', 'Не розпочата'), ('i', 'Розпочата'), ('c', 'Завершена')], default='n', max_length=1),
        ),
    ]
