from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('task_lists/', views.TaskLists.as_view()),
    path('task_lists/<int:pk>/', views.TaskListDetails.as_view()),
    path('task_lists/<int:fk>/tasks/', views.Tasks.as_view()),
    path('tasks/<int:pk>/', views.TaskDetails.as_view()),
]