# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-20 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_task_overdue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='promizhny_control',
            field=models.IntegerField(default=50, help_text='введіть процент, якій провіряє від кінця терміну завершення завдання, коли потрібно включати проміжний контроль (за замовчуванням 50%). Наприклад, якщо бажаєте, щоб завданнє за 30% до кінця строку повина буде включена в проміжний контрол, зменіть процент до 30.', verbose_name='Процент Проміжного Контролю'),
        ),
        migrations.AlterField(
            model_name='task',
            name='overdue',
            field=models.BooleanField(default=True, verbose_name='Прострочена'),
        ),
        migrations.AlterField(
            model_name='task',
            name='promizhny',
            field=models.BooleanField(default=True, verbose_name='Контроль'),
        ),
    ]