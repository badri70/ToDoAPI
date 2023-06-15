from django.shortcuts import render
from rest_framework import generics
from task.models import Task
from .serializers import TaskSerializer


# Create your views here.
class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer