from django.urls import path
from .views import (index,
                    TaskListView,
                    TaskCreateView,
                    TaskUpdateView,
                    TaskDeleteView,
                    TagListView,
                    TagCreateView,
                    TagUpdateView,
                    TagDeleteView,
                    ToggleCompleteTaskView,
                    )

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/create/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/<int:pk>/toggle-complete/", ToggleCompleteTaskView.as_view(), name="toggle-complete-task")

]
app_name = "todo"
