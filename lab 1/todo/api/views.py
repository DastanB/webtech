from django.shortcuts import render
from .models import Task, TaskList
from .serializers import TaskListSerializer, TaskSerializer, ShortTaskSerializer

from rest_framework import static
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class TaskLists(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class TaskListDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class Tasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(task_list = TaskList.objects.get(pk=self.kwargs["fk"]))
    
    def perform_create(self, serializer):
        serializer.save(task_list = TaskList.objects.get(pk=self.kwargs["fk"]))

class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer