from rest_framework import serializers

from .models import Task


class TaskDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор Задачи - сериализация модели конкретной Задачи """
    class Meta:
        model = Task
        fields = '__all__'
