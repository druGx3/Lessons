def task_to_dict(task):
    return {
        'id': task.id,
        'name': task.name,
        'plan': task.plan,
        'complete': task.complete,
        'progress': task.progress,
        'status': task.status(),
    }
def format_task_text(task):
    return f"ID: {task.id} | {task.name} - {task.complete}/{task.plan} - {task.progress}% - {task.status()}"