import json
from datetime import date
from uuid import UUID
from exceptions import StorageError
from models import Task

def load_tasks():
    info = []
    errors = []
    try:
        with open ("task.json", "r", encoding="utf-8") as file:
            try:
                n = json.load(file)
            except json.JSONDecodeError as error:
                raise StorageError(f"Ошибка в формате JSON: {error}")
            for i, task in enumerate(n):
                try:
                    task_id = None

                    task_id = UUID(task["id"]) if "id" in task else None

                    correct = Task(task["name"], task["plan"], task["complete"],date.fromisoformat(task["date"]),task_id)
                    info.append(correct)
                except (ValueError, KeyError) as error:
                    if task_id is not None:
                        errors.append(f"Запись №{i + 1}\nID: {task_id}\nОшибка: {error}")
                    else:
                        errors.append(f"Запись №{i + 1}\nОшибка: {error}")

    except FileNotFoundError:
        print("Файл task.json не найден. Создаём новый.")
        with open("task.json", "w") as file:
            json.dump([], file)
    return info, errors
def save_tasks(tasks):
    tasks_data = []
    for task in tasks:
        task_data = {
            'name': task.name,
            'plan': task.plan,
            'complete': task.complete,
            'date': task.date.isoformat(),
            'id': str(task.id)
        }
        tasks_data.append(task_data)

    with open("task.json", "w", encoding="utf-8") as file:
        json.dump(tasks_data, file, ensure_ascii=False, indent=4)