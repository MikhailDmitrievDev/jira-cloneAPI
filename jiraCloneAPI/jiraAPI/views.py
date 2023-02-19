from rest_framework import generics, viewsets

from .serializers import *


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
