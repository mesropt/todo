from uuid import uuid4

from django.db import models


class Author(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(
        self,
    ):  # Это переопределение метода __Str__. Это магический метод, который у объекта возвращает его строковое представлеине. То есть если я захочу вывести объект класс Author, то он покажет просто name автора (если это единичный объект), если же это список объектов, то я получу список name (имен) авторов. то есть, чтобы выводилось хорошее красивое имя.
        return self.last_name


class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, models.PROTECT)
