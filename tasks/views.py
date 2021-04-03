from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    return HttpResponse('Hello word!')


def taskList(request):
    return render(request, 'tasks/task_list.html')


def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})