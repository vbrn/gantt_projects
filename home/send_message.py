from django.core.mail import send_mail
from home.models import TASK, CONTROL
from django.shortcuts import get_list_or_404
import datetime

def send_message():
    #send_mail('subject', 'body of the message', 'sender@example.com', ['receiver1@example.com', 'receiver2@example.com'])
    #fixing bug https://accounts.google.com/DisplayUnlockCaptcha
    #https://myaccount.google.com/lesssecureapps 
    promizhny = TASK.objects.all().filter(promizhny=False)
    overdue = TASK.objects.all().filter(overdue=False)
    if promizhny or overdue:
        if not promizhny: promizhny_message = ""
        else: promizhny_message ="Завдання на Проміжному Контролі:\n" + "\n ".join([ ("{}".join([str(__), _.name_task, _.project.name, _.start.isoformat(), _.finish.isoformat()])+'.').format(') ', '. Проект: ', '. Дата початку: ', '. Дата завершення: ') for __,_ in enumerate(promizhny, 1)])
        if not overdue: overdue_message = ""
        else: overdue_message ="Прострочени Завдання:\n" + "\n ".join([ ("{}".join([str(__), _.name_task, _.project.name, _.start.isoformat(), _.finish.isoformat()])+'.').format(') ', '. Проект: ', '. Дата початку: ', '. Дата завершення: ') for __,_ in enumerate(overdue, 1)])
        MESSAGE = "Шановний, {}\n Вот ваш {} звіт:\n\n"+promizhny_message+"\n\n"+overdue_message
        users = CONTROL.objects.all().filter(status='d')
        if users:
                for user in users:
                    send_mail('Щоденний Звіт '+ datetime.datetime.now().date().isoformat(), MESSAGE.format(user.name_admin, "щоденний"), 'gantt.manage@gmail.com', [user.email], fail_silently=False)

        if datetime.datetime.now().weekday() == 3:
            users = CONTROL.objects.all().filter(status='w')
            if users:
                for user in users:
                    send_mail('Щонедільний Звіт '+datetime.datetime.now().date().isoformat(), MESSAGE.format(user.name_admin, "щонедільний"), 'gantt.manage@gmail.com', [user.email], fail_silently=False)

        if datetime.datetime.now().day == 1:
            users = CONTROL.objects.all().filter(status='m')
            if users:
                for user in users:
                    send_mail('Шомісячний Звіт '+datetime.datetime.now().date().isoformat(), MESSAGE.format(user.name_admin, "щомісячний"), 'gantt.manage@gmail.com', [user.email], fail_silently=False)


    #send_mail('subject','Звіт '+datetime.datetime.now().ctime(), 'gantt.manage@gmail.com', ['vbrn@i.ua'],fail_silently=False)

