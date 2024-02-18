from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
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
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")
