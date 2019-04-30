from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')

    def __str__(self):
        return self.name

    def is_owner(self, request):
        return self.user.id == request.user.id

class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    due_on = models.DateTimeField()
    status = models.BooleanField(default=False)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return '{}: {}'.format(self.name, self.created_at)

    def is_owner(self, request):
        return self.user.id == request.user.id