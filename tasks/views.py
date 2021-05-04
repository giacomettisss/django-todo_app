from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import TaskForm
from .models import Task

# Create your views here.

def test(request):
    return HttpResponse('Hello word!')


def taskList(request):

    tasks = Task.objects.all().order_by('-created_at')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()

            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'tasks/newtask.html', {'form': form})

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form =  TaskForm(instance=task)

    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if (form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    message = 'Task deleted with success.'
    messages.info(request, message)

    return redirect('/')

def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})

