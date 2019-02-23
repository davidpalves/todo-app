from rest_framework import viewsets
from .models import Todo, Task
from .serializers import TodoSerializer, TaskSerializer
from django.db.models import Q


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.id is not None:
            todos = Todo.objects.filter(
                Q(owner_id=user.id) |
                Q(contributors__id=user.id)
                )
        else:
            todos = Todo.objects.none()
        return todos

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
