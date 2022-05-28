from django_filters import rest_framework as filters
from .models import Project, ToDo


# Фильтрация по части названия проекта
class ProjectFilter(filters.FilterSet):
    proejct_name = filters.CharFilter(lookup_expr='contains') # Здесь указано как фильтровать.

    class MetA:
        model = Project
        fields = ['project_name'] # Здесь указано какие поля фильтровать.

# Фильтрация по проекту:
class ToDoFilter(filters.FilterSet):
    proejct_name = filters.CharFilter(lookup_expr='contains')

    class MetA:
        model = ToDo
        fields = ['project_name']