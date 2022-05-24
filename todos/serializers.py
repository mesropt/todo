from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Project, ToDo
from abc import ABC

class UserListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return f'{value.get_username()}'

    def to_internal_value(self, data):
        obj = get_user_model().objects.get(username=data)
        return obj


class ProjectModelSerializer(serializers.ModelSerializer):
    users = UserListingField(many=True, queryset=get_user_model().objects.all())

    class Meta:
        model = Project
        fields = '__all__'

class ToDoModelSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    execution_status = serializers.BooleanField(read_only=True)
    project_name = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = ToDo
        fields = '__all__'