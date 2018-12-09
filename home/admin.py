from django.contrib import admin

from .models import PROJECT, TASK, CONTROL



# Register your models here.
#admin.site.register(PROJECT)
admin.site.register(CONTROL)

    

@admin.register(PROJECT)
class Project_DB_ADmin(admin.ModelAdmin):
    list_display = ('name', 'responsible', 'created_at','promizhny_control')
    list_filter = ('responsible',)
    class Meta:
        ordering=['created_at']
    
@admin.register(TASK)
class Priznach_DB_Admin(admin.ModelAdmin):
    list_display = ('name_task', 'promizhny', 'overdue','start','promizhny_date','finish','status', 'performer','project')
    list_filter = ('project','performer', 'promizhny','overdue','promizhny_date')
    fieldsets = (
        ('Назва проекту', {'fields': ('project',)}),
        ('Коротка назва завдання (max- 30 символів)', {'fields': ('name_task', )}),
        ("Текст завдання (max-1000 символів, не обов'язкова для заповнення)", {'fields': ('text', )}),
        ('Дати початку і Завершення', {'fields': ('start','finish','promizhny', 'overdue')}),
        ('Статус завдання', {'fields': ('status',)}),
        (None, {'fields': ('performer','overdue_reason','promizhny_date')})

        )
    list_per_page = 10 # pagination
    ordering = ('project_id','id')

