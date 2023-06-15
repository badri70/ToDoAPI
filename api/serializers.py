from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Task
        fields = ['id', 'title', 'memo', 'created_date', 'date_complete', 'important', 'user', 'user_id']
