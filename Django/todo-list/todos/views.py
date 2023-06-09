from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from .forms import TaskForm, TaskModelForm
# Create your views here.


def home(request):
    tasks = Todo.objects.all()
    form = TaskModelForm()
    return render(request, "index.html", {"tasks": tasks,
                                          "form": form})


def salvar(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        form.save()
        messages.success(request, message=f'Task foi criada com sucesso')
        return redirect(home)


def editar(request, task_id):
    task = Todo.objects.get(id=task_id)
    form = TaskModelForm(instance=task)
    return render(request, "update.html", {"task": task,
                                           "form": form})


def update(request, task_id):
    if request.method == 'POST':
        task = Todo.objects.get(id=task_id)
        form = TaskModelForm(request.POST, instance=task)
        form.save()
        messages.success(request, message=f'{task_id} Atualizada com sucesso')
        redirect(home)
    return redirect(home)


def delete(request, task_id):
    task_obj = Todo.objects.get(id=task_id)
    task_obj.delete()
    return redirect(home)
