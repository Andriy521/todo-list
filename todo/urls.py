from django.urls import path

from todo.views import (
    TaskListView,
    TagListView,
    undo_task,
    complete_task
)

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('tags/', TagListView.as_view(), name='tags_list'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('undo/<int:task_id>/', undo_task, name='undo_task')
]
