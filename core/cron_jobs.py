from django_cron import CronJobBase
from django_q.tasks import async_task
from core import tasks

class MyTaskCronJob(CronJobBase):
    RUN_EVERY_MINS = 4320  # 3 days * 24 hours/day * 60 minutes/hour

    def do(self):
        async_task(tasks.my_task, 5)
