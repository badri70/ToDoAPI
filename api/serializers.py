from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'memo', 'created_date', 'date_complete', 'important', 'user']
