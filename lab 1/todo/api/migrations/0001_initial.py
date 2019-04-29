# Generated by Django 2.1.2 on 2019-04-15 11:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 4, 15, 17, 58, 50, 318708))),
                ('due_on', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.TaskList'),
        ),
    ]