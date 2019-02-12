from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from todos.models import Todo, Task
from todos.serializers import TodoSerializer
from django.db.models import Q


class UserSerializer(serializers.ModelSerializer):
    todos = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'username', 'email', 'todos')
        model = User

    def get_todos(self, obj):
        todos = Todo.objects.filter(Q(contributors_id=obj.id) | Q(owner_id=obj.id))
        serializer = TodoSerializer(todos, many=True)
        return serializer.data