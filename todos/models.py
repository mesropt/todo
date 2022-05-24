from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

# Самая важная часть модели - и единственная необходимая часть модели - это список полей базы данных, которые она определяет. Поля определяются атрибутами класса.
# СВЯЗИ ПИШЕМ В МОДЕЛЯХ
# Модель является единственным источником информации о ваших данных. Она содержит основные поля и поведение данных, которые вы храните. Как правило, каждая модель отображается в одну таблицу базы данных.
# Каждый атрибут модели представляет поле базы данных.


class Project(models.Model):  # ПРОЕКТ, ДЛЯ КОТОРОГО ЗАПИСАНЫ ЗАМЕТКИ
    uid = models.UUIDField(primary_key=True, default=uuid4)
    project_name = models.CharField(max_length=64, unique=True, verbose_name="Название проекта")
    repository_link = models.URLField(max_length=200, blank=True, verbose_name="Ссылка на репозиторий")
    users = models.ManyToManyField(
        get_user_model(), verbose_name="пользователи, работающие с проектом"
    )  # Много пользователей - много проектов.


class ToDo(models.Model):  # ЗАМЕТКА
    uid = models.UUIDField(primary_key=True, default=uuid4)
    project_name = models.ManyToManyField(Project, verbose_name="проект, в котором сделана заметка")
    note_text = models.TextField(max_length=64, verbose_name="текст заметки")
    date_created = models.DateTimeField(max_length=64, auto_now_add=True, verbose_name="дата создания")
    date_updated = models.DateTimeField(max_length=254, auto_now=True, verbose_name="дата обновления")
    author = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, verbose_name="автор заметки"
    )  # Одна заметка - один автор.
    execution_status = models.BooleanField(verbose_name="статус активности заметки")
