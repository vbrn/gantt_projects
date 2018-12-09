from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import PROJECT, TASK, CONTROL
from .update_task import update_task
from .send_message import send_message
from .make_news import make_news, one_news, make_human
from .gantt_google import gantt
# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
import datetime
from Crypto.Cipher import AES
import base64
import os


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    model = PROJECT
    context_object_name = 'projects'
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        update_task()
        projects = PROJECT.objects.all().order_by('-pk')
        prom_control_check = lambda _list: True if [_ for _ in _list if  _.promizhny==False] else False
        overdue_check = lambda _list: True if [_ for _ in _list if  _.overdue==False] else False
        kwargs['projects_list'] = [{'project':_, 'date_finish': TASK.objects.all().filter(project=_).order_by('-finish')[0].finish, 'prom_control': prom_control_check(TASK.objects.all().filter(project=_)), 'overdue_control': overdue_check(TASK.objects.all().filter(project=_))} for _ in projects if TASK.objects.all().filter(project=_)]
        return super().get_context_data(**kwargs)

@login_required
def project_detail(request, pk):
    update_task()
    project = PROJECT.objects.get(pk=pk)
    script = gantt(TASK.objects.all().filter(project=project).order_by('-pk'))
    #script = gantt(TASK.objects.all().filter(project=project).order_by('-pk'), name=project.name +". Відповідальний: "+ project.responsible)
    project_tasks = TASK.objects.all().filter(project__pk=pk).order_by('pk')
    #return HttpResponse(str(project.name)+str(project_tasks[0].name_task))
    return render(request, 'project_detail.html',{'project': project, 'project_tasks': project_tasks, 'script': script})


def send_email(request, pk):
    message_text = pk
    secret_key = os.getenv('secret_key')
    cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
    try:
        decoded = cipher.decrypt(base64.b64decode(pk)).decode('utf-8').strip()
        if decoded == (datetime.datetime.now().date().isoformat() + str(datetime.datetime.now().minute)).replace('-','')[::-1]:
            update_task()
            send_message()
        return redirect(reverse('home'))
    except ValueError: return HttpResponse('We dont wanna spam message from you, please, stop, dont do it, dont put yourself in to position to look like fool!!')




@login_required
def news(request):
    return render(request, "news.html", {'begining_news': one_news('education')})

    
#from django.utils import simplejson
from django.http import JsonResponse

def ajax_news(request):
    results = {'success':False}
    key = request.GET.get('key', None)
    # Тут — потрібні нам алгоритми

    param = one_news(key)
    if True:
        results = {'success':True, 'param': param}
    if not key:
        results = {'success':True, 'param': "Сталась якась помилка з нашей сторони, або ваш пристрій посилає несподіваний запит!"}
    return JsonResponse(results)

