from ..models import Task


# method to register a task in the database
def registerTask(task):
    Task.objects.create(title=task.title, description=task.description,
                        expiration_date=task.expiration_date, priority=task.priority)


# method to list all database tasks
def listTasks():
    return Task.objects.all()


# method to list a task by id
def listTaskId(id):
    return Task.objects.get(id=id)


# method for editing a task
def editTask(task_bd, new_task):
    task_bd.title = new_task.title
    task_bd.description = new_task.description
    task_bd.expiration_date = new_task.expiration_date
    task_bd.priority = new_task.priority


# method to remove a task
def removeTask(task_bd):
    task_bd.delete()
