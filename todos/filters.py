from django_filters import rest_framework as filters
from .models import Project, ToDo


# Фильтрация по части названия проекта
class ProjectFilter(filters.FilterSet):
    project_name = filters.CharFilter(lookup_expr='contains') # Здесь указано как фильтровать.

    class Meta:
        model = Project
        fields = ['project_name'] # Здесь указано какие поля фильтровать.

# Фильтрация по проекту:
class ToDoFilter(filters.FilterSet):
    project_name = filters.CharFilter(field_name='project_name', lookup_expr='contains')
    date = filters.DateFromToRangeFilter(field_name='date_created')

    class Meta:
        model = ToDo
        fields = ['project_name']