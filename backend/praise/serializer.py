from asyncio import Task
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from .models import User, Voices, Tasks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 'username')

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ("id", "user_id", "title", "deadline", "target_datetime", "notificate_at", "memo", "is_closed")

class VoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voices
        fields = ("title", "id", "user_id", "file_path")