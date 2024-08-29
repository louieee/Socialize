from django_q.tasks import async_task

def my_task(param):
    # Task logic here
    print(f"Processing {param}")

