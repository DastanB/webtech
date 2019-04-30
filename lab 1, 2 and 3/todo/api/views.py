from django.shortcuts import render
from .models import Task, TaskList
from .serializers import TaskListSerializer, TaskSerializer, ShortTaskSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework import static
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        User.objects.create(username=username, email=email)
        user = User.objects.get(username=username)
        User.set_password(user, raw_password=password)
        user.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response({"errors": "Invalid data"})

class TaskLists(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get_queryset(self):
        return TaskList.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskListDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get_object(self):
        return TaskList.objects.filter(user=self.request.user).get(id=self.kwargs['pk'])


    def perform_update(self, serializer):
        if self.get_object().is_owner(self.request):
            serializer.save()

    def perform_destroy(self, instance):
        if self.get_object().is_owner(self.request):
            instance.delete()


class Tasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    
    def get_queryset(self):
        return Task.objects.filter(task_list = TaskList.objects.get(pk=self.kwargs["fk"]), user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(task_list = TaskList.objects.get(pk=self.kwargs["fk"]), user=self.request.user)

class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get_object(self):
        return Task.objects.filter(user=self.request.user).get(id=self.kwargs['pk'])


    def perform_update(self, serializer):
        if self.get_object().is_owner(self.request):
            serializer.save()

    def perform_destroy(self, instance):
        if self.get_object().is_owner(self.request):
            instance.delete()