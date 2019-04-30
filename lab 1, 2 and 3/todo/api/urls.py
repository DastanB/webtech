from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('task_lists/', views.TaskLists.as_view()),
    path('task_lists/<int:pk>/', views.TaskListDetails.as_view()),
    path('task_lists/<int:fk>/tasks/', views.Tasks.as_view()),
    path('tasks/<int:pk>/', views.TaskDetails.as_view()),
]