from abc import ABC
from rest_framework import serializers
from .models import Project, ToDo


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


# ------------------------------
class ToDoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"
