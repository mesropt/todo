from rest_framework import serializers

from .models import Article, Author, Biography, Book


class AuthorModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BiographyModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = "__all__"


class ArticleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class BookModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
