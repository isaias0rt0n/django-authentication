from django.urls import path
from .views.taskViews import *

urlpatterns = [
    path('listar_tarefas/', listTasks, name='listar-tarefas'),
    path('cadastrar_tarefa/', registerTask, name='cadastrar_tarefa'),
    path('editar_tarefa/<int:id>', editTask, name='editar_tarefa'),
    path('remover_tarefa/<int:id>', removeTask, name='remover_tarefa'),
]
