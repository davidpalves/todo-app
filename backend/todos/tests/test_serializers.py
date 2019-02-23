from django.test import TestCase
from todos.models import Todo, Task
from django.utils import timezone
from todos import serializers
from model_mommy import mommy
from rest_framework.exceptions import ValidationError


class TodoSerializerTests(TestCase):
    def setUp(self):
        self.owner = mommy.make('User')
        self.todo = mommy.make(
            Todo,
            title='todo test',
            owner=self.owner,
            contributors=[mommy.make('User', make_m2m=True)],
            tasks=[]
        )

    def test_todo_contains_expected_fields(self):
        self.serializer = serializers.TodoSerializer(instance=self.todo)
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(
            ['id', 'title', 'owner', 'contributors', 'tasks']))

    def test_todo_serializer_with_data(self):
        data = {
            'title': 'todo test serializer',
            'owner': self.owner.id
        }

        serializer = serializers.TodoSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_todo_serializer_without_title(self):
        data = {
            'owner': self.owner.id
        }
        with self.assertRaises(ValidationError):
            serializer = serializers.TodoSerializer(data=data)
            serializer.is_valid(raise_exception=True)


class TaskSerializerTests(TestCase):
    def setUp(self):
        self.responsible = mommy.make('User')
        self.todo = mommy.make(
            Todo,
            title='todo test',
            owner=mommy.make('User'),
            contributors=[mommy.make('User', make_m2m=True)],
            )
        self.task = mommy.make(
            Task,
            title='test task',
            description='test description',
            deadline=timezone.now(),
            done=False,
            responsible=self.responsible,
            todo=self.todo
        )

    def test_task_contains_expected_fields(self):
        self.serializer = serializers.TaskSerializer(instance=self.task)
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(
            ['id', 'title', 'description', 'deadline',
             'done', 'responsible', 'todo']
        ))

    def test_task_serializer_with_data(self):
        data = {
            'title': 'task test serializer',
            'description': 'test description',
            'deadline': timezone.now(),
            'done': False,
            'responsible': self.responsible.id,
            'todo': self.todo.id
            }

        serializer = serializers.TaskSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_task_serializer_without_title(self):
        data = {
            'description': 'test description',
            'deadline': timezone.now(),
            'done': False,
            'responsible': self.responsible.id,
            'todo': self.todo.id
        }

        with self.assertRaises(ValidationError):
            serializer = serializers.TaskSerializer(data=data)
            serializer.is_valid(raise_exception=True)
