from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from todos.models import Todo, Task
from todos.serializers import TodoSerializer
from django.db.models import Q


class UserSerializer(serializers.ModelSerializer):
    todos = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'username', 'email', 'todos', 'tasks')
        model = User

    def get_todos(self, obj):
        todos = Todo.objects.filter(Q(contributors__id=obj.id) | Q(owner_id=obj.id))
        serializer = TodoSerializer(todos, many=True)
        return serializer.data

    def get_tasks(self, obj):
        tasks = Task.objects.filter(responsible_id=obj.id)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        

