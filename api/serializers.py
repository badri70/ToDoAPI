from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    date_complete = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'memo', 'created_date', 'date_complete', 'important', 'user', 'user_id']


class TaskCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id']
        read_only_fields = ['title', 'memo', 'created_date', 'date_complete', 'important', 'user', 'user_id']