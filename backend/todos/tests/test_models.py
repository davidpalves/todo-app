from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone
from model_mommy import mommy

from todos.models import Task, Todo


class TodoModelTestCase(TestCase):
    def setUp(self):
        self.owner = mommy.make(
            User,
            username="test",
            password="test123"
            )

        self.contrib = mommy.make(
            User,
            username="contributor",
            password="contributor123"
            )

        self.todo = mommy.make(
            Todo,
            title="Test todo",
            owner=self.owner,
            )

        self.todo.contributors.add(self.contrib)

    def test_todo_creation(self):
        self.assertTrue(Todo.objects.get(title='Test todo'))

    def test_todo_title(self):
        self.assertEqual('Test todo', str(self.todo))

    def test_todo_owner(self):
        self.assertEqual('test', self.owner.username)

    def test_todo_contributors(self):
        self.assertEqual(
            'contributor', self.todo.contributors.first().username
            )

    def test_todo_without_title(self):
        with self.assertRaises(IntegrityError):
            Todo.objects.create(owner=self.owner)

    def test_todo_without_owner(self):
        with self.assertRaises(IntegrityError):
            Todo.objects.create(title='Teste 2')


class TaskModelTestCase(TestCase):
    def setUp(self):
        self.owner = mommy.make(
            User,
            username="test",
            password="test123"
            )

        self.responsible = mommy.make(
            User,
            username="responsible",
            password="responsible123"
            )

        self.todo = mommy.make(
            Todo,
            title="Test todo",
            owner=self.owner,
            )

        Task.objects.create(
            title='Test task',
            description='Description test',
            deadline=timezone.now(),
            responsible=self.responsible,
            todo=self.todo
        )
        self.task = Task.objects.get(title='Test task')

    def test_task_creation(self):
        self.assertTrue(Task.objects.get(title='Test task'))

    def test_task_title(self):
        self.assertEqual('Test task', str(self.task))

    def test_task_description(self):
        self.assertEqual('Description test', self.task.description)

    def test_task_done_false(self):
        self.assertFalse(self.task.done)

    def test_task_done_true(self):
        self.task.done = True
        self.assertTrue(self.task.done)

    def test_task_responsible(self):
        self.assertEqual('responsible', self.responsible.username)

    def test_task_todo(self):
        self.assertEqual('Test todo', str(self.task.todo))

    def test_task_without_title(self):
        with self.assertRaises(IntegrityError):
            Task.objects.create(todo=self.todo)

    def test_task_without_todo(self):
        with self.assertRaises(IntegrityError):
            Task.objects.create(title='Test task')
