from django.urls import path
from .views.taskViews import *
from .views.userViews import *

urlpatterns = [
    path('listar_tarefas/', listTasks, name='listar-tarefas'),
    path('cadastrar_tarefa/', registerTask, name='cadastrar_tarefa'),
    path('editar_tarefa/<int:id>', editTask, name='editar_tarefa'),
    path('remover_tarefa/<int:id>', removeTask, name='remover_tarefa'),

    path('cadastrar_usuario/', registerUser, name='cadastrar_usuario'),
    path('login_usuario/', loginUser, name='logar_usuario'),
    path('deslogar_usuario/', logoffUser, name='deslogar_usuario'),
]
