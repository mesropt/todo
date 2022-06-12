from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAdminUser, IsAuthenticated, \
    IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .filters import ProjectFilter, ToDoFilter
from .models import Project, ToDo
from .pagination import ProjectLimitOffsetPagination, ToDoLimitOffsetPagination
from .serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]


# ------------------------------
class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
