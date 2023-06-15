from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from task.models import Task
from .serializers import TaskSerializer
from rest_framework.exceptions import ValidationError


# Create your views here.
class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user, date_complete__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user, pk=self.kwargs['pk'])
        if queryset.exists():
            return queryset
        raise ValidationError("Sorry this task not founded!")

    def put(self, request, *args, **kwargs):
        if not self.get_queryset().exists():
            raise ValidationError("Sorry it's not your task!")
        self.update(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        if not self.get_queryset().exists():
            raise ValidationError("Sorry it's not your task!")
        self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)