from django.shortcuts import render, redirect

from ..forms import TaskForm
from ..services import taskService
from ..entities.task import Task


def listTasks(request):
    tasks = taskService.listTasks()
    return render(request, 'tasks/list_tasks.html', {"tasks": tasks})


def registerTask(request):
    if request.method == "POST":
        form_task = TaskForm(request.POST)
        if form_task.is_valid():
            title = form_task.cleaned_data["title"]
            description = form_task.cleaned_data["description"]
            expiration_date = form_task.cleaned_data["expiration_date"]
            priority = form_task.cleaned_data["priority"]
            new_task = Task(title=title, description=description,
                            expiration_date=expiration_date, priority=priority)
            taskService.registerTask(new_task)
            return redirect('listar-tarefas')
    else:
        form_task = TaskForm()
    return render(request, 'tasks/form_task.html', {"form_task": form_task})


def editTask(request, id):
    task_bd = taskService.listTaskId(id)
    form_task = TaskForm(request.POST or None, instance=task_bd)
    if form_task.is_valid():
        title = form_task.cleaned_data["title"]
        description = form_task.cleaned_data["description"]
        expiration_date = form_task.cleaned_data["expiration_date"]
        priority = form_task.cleaned_data["priority"]
        new_task = Task(title=title, description=description,
                        expiration_date=expiration_date, priority=priority)
        taskService.editTask(task_bd, new_task)
        return redirect('listar-tarefas')
    return render(request, 'tasks/form_task.html', {'form_task': form_task})


def removeTask(request, id):
    task_bd = taskService.listTaskId(id)
    if request.method == "POST":
        taskService.removeTask(task_bd)
        return redirect('listar-tarefas')
    return render(request, 'tasks/confirma_exclusao.html', {'task': task_bd})
