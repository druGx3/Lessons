from input_utils import (
    get_task_date,
    get_int_input,
    get_uuid_input
)
from planner.exceptions import StorageError
from storage import load_tasks, save_tasks
from services import (
    add_task,
    update_task_complete,
    delete_task,
    get_tasks,
    get_today_tasks,
    find_tasks_by_date,
)
from views import format_task_text


def show_menu():
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Изменить прогресс")
    print("4. Удалить задачу")
    print("5. Показать сегодняшние задачи")
    print("6. Найти задачу по дате")
    print("7. Выйти")

def handle_choice(choice, tasks):
    actions = {
        "1": show_tasks_menu,
        "2": add_task_menu,
        "3": update_task_menu,
        "4": delete_task_menu,
        "5": show_today_tasks_menu,
        "6": find_by_date_menu,
    }
    if choice == "7":
        return False
    if choice in actions:
        actions[choice](tasks)
    else:
        print("Введите известное вам действие")
    return True

def show_today_tasks_menu(tasks):
    today_tasks = get_today_tasks(tasks)
    if today_tasks:
        for task in today_tasks:
            print(format_task_text(task))
    else:
        print("Задач сегодня нет")

def show_tasks_menu(tasks):
    all_tasks = get_tasks(tasks)
    for task in all_tasks:
        print(format_task_text(task))

def update_task_menu(tasks):
    while True:
        task_id = get_uuid_input()

        new_complete = get_int_input(
            "Введите новое количество выполненного: ",
            "Введите число для выполненного"
        )

        try:
            result = update_task_complete(tasks, task_id, new_complete)
            if result:
                print(f"Задача обновлена\n{result.name}\n{result.progress}%")
                break
            else:
                print("Задача не найдена!")
        except ValueError as error:
            print(error)

def add_task_menu(tasks):
    while True:
        name = input("Введите имя: ")

        plan = get_int_input(
            "Введите план: ",
            "Введите число для плана"
        )
        complete = get_int_input(
            "Введите количество выполненного: ",
            "Введите число для выполненного"
        )
        user_date = get_task_date()
        try:
            new_task = add_task(tasks, name, plan, complete, user_date)
            print(f"Новая задача:\n{format_task_text(new_task)}")
            break
        except ValueError as error:
            print(error)

def delete_task_menu(tasks):
    task_id = get_uuid_input()

    removing = delete_task(tasks, task_id)

    if removing:
        print(f"Задача успешно удалена\nУдаленная задача:\n{format_task_text(removing)}")
    else:
        print("Задача не была найдена")

def find_by_date_menu(tasks):
    user_date = get_task_date()
    result = find_tasks_by_date(tasks, user_date)
    if result:
        for task in result:
            print(format_task_text(task))
    else:
        print("Задач на этот день нет")


def main():
    try:
        tasks, errors = load_tasks()
    except StorageError as error:
        print(error)
        return
    if errors:
        for error in errors:
            print(error)
    while True:
        show_menu()
        choice = input("Выбери действие:")
        if not handle_choice(choice, tasks):
            break
    save_tasks(tasks)
if __name__ == "__main__":
    main()


