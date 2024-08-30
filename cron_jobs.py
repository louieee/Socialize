import logging
import os

import django
import schedule
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Socialize.settings')
django.setup()
from django_q.tasks import async_task
from core import tasks

def do_this():
    value = async_task(tasks.my_task, 5)


schedule.every(10).seconds.do(do_this)

while True:
    schedule.run_pending()
    time.sleep(1)
