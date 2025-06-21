from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm, TagForm
from .models import Task, Tag


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tag_form.html"

class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task_list.html"

    def get_queryset(self):
        return Task.objects.prefetch_related('tags').order_by('is_done', '-datetime')


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('todo:task-list')
