from rest_framework import viewsets

from .serializers import *


class TaskViewSet(viewsets.ModelViewSet):
    """Веб - сервис, CRUD действи с задачей. """

    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
