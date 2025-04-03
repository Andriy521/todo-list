from django.shortcuts import render, redirect
from django.views import generic
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


