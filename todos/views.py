from rest_framework.viewsets import ModelViewSet

from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer
from .pagination import ProjectLimitOffsetPagination, ToDoLimitOffsetPagination

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination