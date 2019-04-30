from rest_framework.serializers import ModelSerializer
from .models import Task, TaskList
from django.contrib.auth.models import User

class TaskListSerializer(ModelSerializer):
    class Meta:
        model = TaskList
        fields = ['id', 'name']

class TaskSerializer(ModelSerializer):
    task_list = TaskListSerializer(read_only=True)
    class Meta: 
        model = Task
        fields = ['id', 'name', 'created_at', 'due_on', 'status', 'task_list']

class ShortTaskSerializer(ModelSerializer):
    class Meta: 
        model = Task
        fields = ['id', 'name', 'status']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']