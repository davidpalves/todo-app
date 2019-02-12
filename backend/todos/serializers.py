from rest_framework import serializers
from .models import Todo, Task


class TodoSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    class Meta:
        fields = (
            'id',
            'title',
            'owner',
            'contributors',
            'tasks',
        )
        model = Todo

    def get_tasks(self, obj):
        tasks = Task.objects.filter(todo_id=obj.id)
        serializer = TaskSerializer(tasks, many=True)
        return serializer.data

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'deadline',
            'done',
            'todo'
        )
        model = Task
    