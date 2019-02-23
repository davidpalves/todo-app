from rest_framework import serializers
from .models import Todo, Task


class TodoSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    owner = serializers.ReadOnlyField(source='owner.id')
    title = serializers.CharField(
        max_length=200, allow_blank=False, required=True
    )

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
    title = serializers.CharField(
        max_length=140, allow_blank=False, required=True
    )

    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'responsible',
            'deadline',
            'done',
            'todo'
        )
        model = Task
