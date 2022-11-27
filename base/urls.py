from django.urls import path
from .views import TaskList, DetailTask, TaskCreate


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', DetailTask.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='tasks-create'),
]