from datetime import date
from uuid import uuid4

class Task:
    def __init__(self, name, plan, complete, task_date = None, task_id = None):
        if task_date is None:
            self.date = date.today()
        else:
            self.date = task_date

        self.name = name

        self._complete = 0

        self.plan = plan

        self.complete = complete
        if task_id is None:
            self.id = uuid4()
        else:
            self.id = task_id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Название задачи должно быть строкой")
        if not value.strip():
            raise ValueError("Название задачи не может быть пустым")
        self._name = value.strip()

    def validity_complete_non_negative(self, complete):
        if complete < 0:
            raise ValueError("Выполненное количество не может быть отрицательным")

    def validity_check_plan(self, plan):
        if plan <= 0:
            raise ValueError("План не может быть меньше нуля")


    @property
    def plan(self):
        return self._plan

    @plan.setter
    def plan(self, value):
        self.validity_check_plan(value)
        if value < self.complete:
            raise ValueError("Новый план не может быть меньше выполненного количества")
        self._plan = value

    @property
    def complete(self):
        return self._complete

    @complete.setter
    def complete(self, value):
        self.validity_complete_non_negative(value)

        if value > self.plan:
            raise ValueError("Выполненное количество не может быть больше плана")

        self._complete = value

    def status(self):
        if self.complete >= self.plan:
            return "Выполнено"
        elif self.complete == 0:
            return "Не начато"
        else:
            return "В процессе"

    @property
    def progress(self):
        return int(self.complete / self.plan * 100)