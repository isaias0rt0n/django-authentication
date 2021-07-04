from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def registerUser(request):
    if request.method == "POST":
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('listar-tarefas')
    else:
        form_user = UserCreationForm()
    return render(request, 'users/form_user.html', {"form_user": form_user})


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar-tarefas')
        else:
            messages.error(request, 'As credenciais estão incorretas')
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'users/login.html', {"form_login": form_login})


def logoffUser(request):
    logout(request)
    return redirect('logar_usuario')
