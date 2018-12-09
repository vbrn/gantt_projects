from django.db import models
import datetime

# Create your models here.
# check more on https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Models

class CONTROL(models.Model):
    name_admin = models.CharField(max_length = 50, verbose_name="Ім'я",help_text="Введіть ім'я, кому посилати звіт (система буде к ньйому звертатися)" )
    email = models.EmailField(verbose_name="Електронна Пошта", help_text="введіть е-мейл, которому нужно посилати звіт")
    status_choice= (('d', 'Кожний день'),
            ('w','Раз на тиждень'),
            ('m','Раз на місяць'),
            ('n', 'Не посилати мені звіт'))
    status = models.CharField(max_length=1, choices=status_choice, default='n', verbose_name = "Коли вам посилати звіт")
    def __str__(self):
        return self.name_admin
    class Meta:
        verbose_name = "розсилка звіту"
        verbose_name_plural = "розсилка звіту"
    
    

class PROJECT(models.Model):
    name = models.CharField(max_length=500, verbose_name="Назва",help_text="Введіть назву проекту")
    responsible = models.CharField(max_length=200, verbose_name="Відповідальний",  help_text="Введіть головного відповідального за проект", default="Відсутні дані")
    promizhny_control = models.IntegerField(default=50, verbose_name = "Процент Проміжного Контролю", help_text="введіть процент, якій провіряє від кінця терміну завершення завдання, коли потрібно включати проміжний контроль (за замовчуванням 50%). Наприклад, якщо бажаєте, щоб завданнє за 30% до кінця строку повина буде включена в проміжний контрол, зменіть процент до 30.")
    change_percent = models.BooleanField(default=False, verbose_name = "Змінити процент")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Проекти (назви і відповідальні)"
        verbose_name_plural = "Проекти (назви і відповідальні)"

class TASK(models.Model):
    name_task = models.CharField(max_length=30)
    text = models.TextField(max_length=1000, blank=True,null=True)
    start = models.DateField()
    finish = models.DateField()
    project =  models.ForeignKey(PROJECT, related_name='project')
    performer = models.CharField(max_length=1000, verbose_name="Виконавець", help_text="Введіть виконавця завдання, або через кому, якщо їх декілька", default="Відсутні дані")
    overdue_reason = models.CharField(max_length=1000, verbose_name="Причина простроченого завдання", help_text="Якщо завдання прострочено, вкажіть причину, чому це сталося", blank=True, null=True)
    promizhny = models.BooleanField(default=True, verbose_name = "Не на контролi")
    promizhny_date = models.DateField(default = datetime.date(1,1,1), verbose_name = "Дата контролю")
    overdue = models.BooleanField(default=True, verbose_name = "Не прострочена")
    status_choice= (('n', 'Не розпочата'),
            ('i','Розпочата'),
            ('c','Завершена'))
    
    status = models.CharField(max_length=1, choices=status_choice, default='n')
    def __str__(self):
        return self.name_task
    class Meta:
        verbose_name = "Завдання проектів"
        verbose_name_plural = "Завдання проектів (деталі)"


