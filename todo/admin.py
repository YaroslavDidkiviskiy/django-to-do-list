from django.contrib import admin

from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "datetime", "deadline", "is_done",]
    list_filter = ["tags",]
    search_fields = ["content",]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]
    list_filter = ["name",]
