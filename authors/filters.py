from django_filters import rest_framework as filters
from .models import Author, Biography, Article, Book


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birthday_year']


class BiographyFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Biography
        fields = ['text', 'author']


class ArticleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Article
        fields = ['name', 'author']


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Book
        fields = ['name', 'authors']