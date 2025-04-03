from django.urls import path

from todo.views import (
    TaskListView,
    TagListView,
    undo_task,
    complete_task,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path("tasks/create/", TaskCreateView.as_view(), name='task-create'),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name='task-update'),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name='task-delete'),
    path('tags/', TagListView.as_view(), name='tags-list'),
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/update/<int:pk>/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/delete/<int:pk>/', TagDeleteView.as_view(), name='tag-delete'),
    path('complete/<int:task_id>/', complete_task, name='complete-task'),
    path('undo/<int:task_id>/', undo_task, name='undo-task')
]
