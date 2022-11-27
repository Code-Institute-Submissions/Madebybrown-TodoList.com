from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Task
from django.urls import reverse_lazy


class TaskList(ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'


class DetailTask(DetailView):
    model = Task
    template_name = 'base/task_detail.html'
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    template_name = 'base/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')
