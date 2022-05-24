from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorModelSerializer, BiographyModelSerializer, ArticleModelSerializer, BookModelSerializer
from .models import Author, Biography, Book, Article

# Это вьюшка, написанная через классы. Вьюшка ещё может быть написана через функцию, но это не комильфо.
class AuthorModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer] # Это мы задали доступные для данного ViewSet рендеры. По умолчанию доступны все глобальные рендеры.
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer

class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer