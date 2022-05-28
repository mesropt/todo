from django_filters import rest_framework as filters
from .models import User


class UserFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains') # Здесь указано как фильтровать.

    class MetA:
        model = User
        fields = ['name'] # Здесь указано какие поля фильтровать.