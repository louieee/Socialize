import logging
import random

from django_q.tasks import async_task

def my_task(param):
    # Task logic here
    value = param + random.randint(0, 99)
    logging.critical(f"Processing {value}")
    with open("new_file.txt", 'w') as file:
        file.write(str(value))
    return


