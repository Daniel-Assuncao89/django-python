from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TaskForm
# Create your views here.


def home(request):
    tasks = Todo.objects.all()
    form = TaskForm()
    return render(request, "index.html", {"tasks": tasks,
                                          "form": form})


def salvar(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task2 = form.cleaned_data['task']
            status2 = form.cleaned_data['status']
            task_create = Todo.objects.create(task=task2, status=status2)
            task_create.save()
            messages.success(request, message=f'{task_create} foi criada com sucesso')
            return redirect(home)




def editar(request, task_id):
    task = Todo.objects.get(id=task_id)
    status = Todo.CHOICE_STATUS
    return render(request, "update.html", {"task": task,
                                           "status": status})


def update(request, task_id):
    task_html = request.POST.get("task")
    status_html = request.POST.get("choices")
    print(status_html)
    task_obj = Todo.objects.get(id=task_id)
    task_obj.task = task_html
    task_obj.status = status_html
    task_obj.save()
    return redirect(home)


def delete(request, task_id):
    task_obj = Todo.objects.get(id=task_id)
    task_obj.delete()
    return redirect(home)
