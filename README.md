# gantt_projects
This is Gantt Chart Projects/Tasks Control System (Система Управления Проектами с диаграмой Ганта)
1) Установите виртуальное окружение с python3
2) pip install -r requirements.txt
3) python manage.py createsuperuser
4) Если хотите нову базу данных, удаляете db.sqlite3 и python manage.py migrate
5) Потом заходите в админку и добавляете проекты и задачи с датами контроля.
6) Если захотите, чтобы система рассылала напоминалку о просроченных задачах или задачах на контроле, вставляете свои настройки gmail или другую систему в mysite/settings.py
