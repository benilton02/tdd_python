from datetime import datetime
from .database import insert_task
from itertools import count

def identifier() -> int:
    id = next(count(0))
    return id


def process_date(date: str) -> str:
    return datetime.strptime(date, '%d/%m/%Y')


def new_task(task_name: str, date: str) -> dict:
    """ Insere uma nova task."""
    
    task = {
        'id': identifier(),
        'task_name': task_name,
        'date': process_date(date),
        'status': "TODO"
    }

    result_db = insert_task(task)

    return task


def tasks_list(task_name: str, status: str = ''):
    pass