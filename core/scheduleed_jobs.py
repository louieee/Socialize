from django_q.models import Schedule

# Schedule a task to run every 10 minutes
Schedule.objects.create(
    func='core.tasks.my_task',
    args='["5"]',
    schedule_type=Schedule.MINUTES,
    minutes=10,
)
