from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic

from .models import Tag, Task


def index(request: HttpRequest) -> HttpResponse:
    task_list = Task.objects.all()
    tag_list = Tag.objects.all()
    context = {
        "task_list": task_list,
        "tag_list": tag_list,
    }
    return render(request, "todo/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
