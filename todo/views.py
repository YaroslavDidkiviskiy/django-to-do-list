from django.shortcuts import render
from django.views import generic

from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task_list.html"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "tag_list.html"
