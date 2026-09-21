from fastapi import FastAPI, HTTPException
from storage import load_tasks, save_tasks
from services import (
    get_tasks,
    add_task,
    update_task_complete,
    delete_task
)
from schemas import (
    TaskResponse,
    TaskCreate,
    TaskUpdate,
)
from uuid import UUID
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks_api():
    info = get_tasks(tasks)
    api_tasks_data = []
    for task in info:
        api_task = TaskResponse(
            id = task.id,
            name = task.name,
            plan = task.plan,
            complete = task.complete,
            date = task.date,
            progress = task.progress,
            status = task.status()
        )
        api_tasks_data.append(api_task)
    return api_tasks_data

@app.post("/tasks", response_model = TaskResponse)
def create_task_api(task: TaskCreate):
    try:
        new_task = add_task(tasks, task.name, task.plan, task.complete, task.date)
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    save_tasks(tasks)

    response_task = TaskResponse(
            id = new_task.id,
            name = new_task.name,
            plan = new_task.plan,
            complete = new_task.complete,
            date = new_task.date,
            progress = new_task.progress,
            status = new_task.status()
        )

    return response_task


@app.patch("/tasks/{task_id}", response_model = TaskResponse)
def update_task_api(task_id: UUID, task: TaskUpdate):
    try:
        updated_task = update_task_complete(tasks, task_id, task.complete)
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    if updated_task is None:
        raise HTTPException(
            status_code = 404,
            detail = "Задача не найдена"
        )
    save_tasks(tasks)

    response_task = TaskResponse(
        id = updated_task.id,
        name = updated_task.name,
        plan = updated_task.plan,
        complete = updated_task.complete,
        date = updated_task.date,
        progress = updated_task.progress,
        status = updated_task.status()
    )

    return response_task

@app.delete("/tasks/{task_id}", response_model = TaskResponse)
def delete_task_api(task_id: UUID):

    deleted_task = delete_task(tasks, task_id)

    if deleted_task is None:
        raise HTTPException(
            status_code = 404,
            detail = "Задача не найдена"
        )

    save_tasks(tasks)

    response_task = TaskResponse(
        id= deleted_task.id,
        name= deleted_task.name,
        plan= deleted_task.plan,
        complete= deleted_task.complete,
        date= deleted_task.date,
        progress= deleted_task.progress,
        status= deleted_task.status()
    )

    return response_task

tasks, errors = load_tasks()

