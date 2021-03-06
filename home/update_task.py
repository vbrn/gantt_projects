from .models import TASK, PROJECT
import datetime

total_days = lambda task: (task.finish-task.start).days
percent_p = lambda task: task.project.promizhny_control/100
#percent_p = lambda task: 50/100
days_promizhny = lambda task: int(total_days(task) * percent_p(task))

promizhny_date = lambda task: task.finish - datetime.timedelta(days=days_promizhny(task))

now = lambda: datetime.datetime.now().date()

check_promizhny = lambda task: True if ((now() - task.promizhny_date).days > 0 and  (task.finish - now()).days >= 0) else False
def change_project_percent():
    projects = PROJECT.objects.all().filter(change_percent=True)
    if projects:
        for project in projects:
            tasks = TASK.objects.all().filter(project=project)
            project.change_percent=False
            project.save()
            [exec("task.promizhny_date=datetime.date(1,1,1); task.save()") for task in tasks]

def change_default_promizhny_date():
    base_date = datetime.date(1,1,1)
    task_work = TASK.objects.all().filter(promizhny_date=base_date)
    if task_work:
        [exec("task.promizhny_date=promizhny_date(task); task.save()") for task in task_work]


def update_task():
    change_project_percent()
    change_default_promizhny_date()
    tasks_all = TASK.objects.all()
    tasks = TASK.objects.all().filter(status='n').union(TASK.objects.all().filter(status='i'))
    promizhny_control = [task for task in tasks if check_promizhny(task)]
    overdue_task = [task for task in tasks if (task.finish - now()).days < 0]
    # Сначала отмечаем все задачи к тру, а потом выделяем фалс там где выявлен контроль
    [exec("task.promizhny=True; task.save()") for task in tasks_all]
    [exec("task.overdue=True; task.save()") for task in tasks_all]
    [exec("task.promizhny=False; task.save()") for task in promizhny_control]
    [exec("task.overdue=False; task.save()") for task in overdue_task]

