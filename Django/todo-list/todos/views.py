from django.shortcuts import render
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