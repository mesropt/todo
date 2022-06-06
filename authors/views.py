from rest_framework.permissions import AllowAny
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .filters import ArticleFilter, AuthorFilter, BiographyFilter, BookFilter
from .models import Article, Author, Biography, Book
from .pagination import (
    ArticleLimitOffsetPagination,
    AuthorLimitOffsetPagination,
    BiographyLimitOffsetPagination,
    BookLimitOffsetPagination,
)
from .serializers import ArticleModelSerializer, AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer
from .permissions import staffOnly

# Это вьюшка, написанная через классы. Вьюшка ещё может быть написана через функцию, но это не комильфо.
class AuthorModelViewSet(ModelViewSet):
    renderer_classes = [
        JSONRenderer,
        BrowsableAPIRenderer,
    ]  # Это мы задали доступные для данного ViewSet рендеры. По умолчанию доступны все глобальные рендеры.
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    pagination_class = AuthorLimitOffsetPagination
    filter_class = AuthorFilter
    permission_classes = [AllowAny] # К AuthorModelViewSet будут иметь
    # доступ все пользователи, в том числе анонимы.


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer
    pagination_class = BiographyLimitOffsetPagination
    filter_class = BiographyFilter


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    pagination_class = ArticleLimitOffsetPagination
    filter_class = ArticleFilter
    filter_class = ArticleFilter


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    pagination_class = BookLimitOffsetPagination
    filter_class = BookFilter
