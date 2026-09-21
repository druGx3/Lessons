from datetime import date
from uuid import UUID


def get_task_date():
    while True:
        try:
            user_date = input("Введите дату задачи (ГГГГ-ММ-ДД): ")
            user_date = date.fromisoformat(user_date)
            break
        except ValueError:
            print("Введите корректную дату в формате ГГГГ-ММ-ДД")
    return user_date


def get_int_input(prompt = '', error_message = ''):
    while True:
        try:
            show_message = int(input(prompt))
            return show_message
        except ValueError:
            print(error_message)


def get_uuid_input():
    while True:
        task_id = input("Введите ID задачи: ")
        try:
            task_id = UUID(task_id)
            return task_id
        except ValueError:
            print("Некорректный ID")