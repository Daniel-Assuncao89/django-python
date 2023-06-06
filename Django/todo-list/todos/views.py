from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def home(request):
    tasks = Todo.objects.all()
    return render(request, "index.html", {"tasks": tasks})


def salvar(request):
    task = request.POST.get("task")
    Todo.objects.create(task=task)
    tasks = Todo.objects.all()
    return render(request, "index.html", {"tasks": tasks})


def editar(request, id):
    task = Todo.objects.get(id=id)
    status = Todo.Status.labels
    return render(request, "update.html", {"task": task,
                                           "status": status})


def update(request, id):
    task_html = request.POST.get("task")
    status_html = request.POST.get("choices")
    print(status_html)
    task_obj = Todo.objects.get(id=id)
    task_obj.task = task_html
    task_obj.status = status_html
    task_obj.save()
    return redirect(home)


def delete(request, id):
    task_obj = Todo.objects.get(id=id)
    task_obj.delete()
    return redirect(home)
