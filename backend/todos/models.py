from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200, blank=False, default=None)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owns',
        blank=False,
        null=False)

    contributors = models.ManyToManyField(
        User,
        default=[],
        blank=True,
        related_name='contributions')

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=140, blank=False, default=None)
    description = models.TextField()
    deadline = models.DateTimeField()
    responsible = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
        related_name='tasks')

    todo = models.ForeignKey(
        Todo,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='tasks')

    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
