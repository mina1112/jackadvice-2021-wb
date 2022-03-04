from django.db.models import query
from django.db.models.base import Model
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView, UpdateView
import django_filters
from rest_framework import viewsets, filters
from rest_framework.serializers import Serializer

from .serializer import TasksSerializer, VoicesSerializer, UserSerializer
from .models import User, Tasks, Voices



def index(request):
    """トップ画面"""
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class VoiceViewSet(viewsets.ModelViewSet):
    queryset = Voices.objects.all()
    serializer_class = VoicesSerializer


