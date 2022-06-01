from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter, ToDoFilter
from .models import Project, ToDo
from .pagination import ProjectLimitOffsetPagination, ToDoLimitOffsetPagination
from .serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


# ------------------------------
class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter