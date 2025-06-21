from django.urls import path

from .views import TaskListView, TagListView, TaskCreateView, TaskUpdateView, TagCreateView, TagUpdateView, TagDeleteView, TaskDeleteView, toggle_task_status

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),

    #tags
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),

    #tasks
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
path('task/<int:pk>/toggle/', toggle_task_status, name='toggle-task'),
]