"""serializers."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """task serializer."""

    class Meta:
        """meta."""

        model = Task
        fields = ("id", "title", "description", "completed")
