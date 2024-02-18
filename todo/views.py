from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Tag, Task


def index(request: HttpRequest) -> HttpResponse:
    task_list = Task.objects.all()
    tag_list = Tag.objects.all()
    context = {
        "task_info": task_list,
        "tag_info": tag_list,
    }
    return render(request, "todo/index.html", context=context)
