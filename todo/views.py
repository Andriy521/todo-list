from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag

class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    ordering = ["done_or_not", "-datetime"]
    template_name = "todo/task_list.html"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    ordering = ["name"]
    template_name = "todo/tag_list.html"


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done_or_not = True
    task.save()
    return redirect('home')


def undo_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done_or_not = False
    task.save()
    return redirect('home')


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('home')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('home')


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('home')


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy('tags-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy('tags-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('tags-list')


