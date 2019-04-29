from django.db import models
import datetime
# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    due_on = models.DateTimeField()
    status = models.BooleanField(default=False)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return '{}: {}'.format(self.name, self.created_at)