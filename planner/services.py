from models import Task
from datetime import date

def find_task(tasks, task_id):
    for task in tasks:
        if task.id == task_id:
            return task
    return None

def find_tasks_by_date(tasks, task_date):
    all_tasks_day = []
    for task in tasks:
        if task.date == task_date:
            all_tasks_day.append(task)
    return all_tasks_day

def add_task(tasks, name, plan, complete, task_date):
    new_task = Task(name, plan, complete, task_date)
    tasks.append(new_task)
    return new_task

def update_task_complete(tasks, task_id, new_complete):
    task = find_task(tasks, task_id)

    if task is None:
        return None

    task.complete = new_complete

    return task


def delete_task(tasks, task_id):
    task = find_task(tasks, task_id)

    if task is not None:
        tasks.remove(task)
        return task

    return None

def get_today_tasks(tasks):
    return find_tasks_by_date(tasks, date.today())

def get_tasks(tasks):
    return tasks.copy()


