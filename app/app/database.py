from os import stat


db = []

def insert_task(task = dict):
    pass

def select_task(task_name: str, status: str):
    if not status:
        return [
            task 
            for task in db
            if task_name == task['task_name']
        ]
    return[
        task 
        for task in db 
        if status == task['status']
    ]
    