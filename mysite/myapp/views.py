from django.shortcuts import render, redirect

from .forms import TableForm
from .forms import TaskForm
from .models import Post
from .models import Post1
from .models import Table
from .models import Task


def index(request):
    tasks = Post.objects.order_by('id')
    title = Task.objects.order_by('id')
    task = Task.objects.order_by('id')
    tables = Table.objects.order_by('id')
    return render(request, 'main/index.html', {'tasks': tasks, 'title': title, 'task': task, 'tables': tables})


def a(request):
    tasks = Post.objects.order_by('id')
    task = Post1.objects.order_by('id')
    return render(request, 'main/a.html', {'tasks': tasks, 'task': task})


def contact(request):
    return render(request, 'main/base.html', {'values': ['lorem10', '2312312']})


def table(request):
    error = ''
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка'
    form = TableForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/table.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
