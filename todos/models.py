from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

# Самая важная часть модели - и единственная необходимая часть модели - это список полей базы данных, которые она определяет. Поля определяются атрибутами класса.
# СВЯЗИ ПИШЕМ В МОДЕЛЯХ
# Модель является единственным источником информации о ваших данных. Она содержит основные поля и поведение данных, которые вы храните. Как правило, каждая модель отображается в одну таблицу базы данных.
# Каждый атрибут модели представляет поле базы данных.


class Project(models.Model):  # ПРОЕКТ, ДЛЯ КОТОРОГО ЗАПИСАНЫ ЗАМЕТКИ
    uid = models.UUIDField(primary_key=True, default=uuid4)
    project_name = models.CharField(max_length=64, unique=True, verbose_name="название проекта")
    repository_link = models.URLField(max_length=200, blank=True, verbose_name="ссылка на репозиторий")
    users = models.ManyToManyField(
        get_user_model(), verbose_name="участники проекта"
    )  # Много пользователей - много проектов.

    def __str__(self):
        return self.project_name


class ToDo(models.Model):  # ЗАМЕТКА
    uid = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="проект")
    note_text = models.TextField(blank=True, verbose_name="текст заметки")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="дата " "обновления")
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="todos", null=True, verbose_name="автор"
    )
    execution_status = models.BooleanField(default=True, verbose_name="статус исполнения", db_index=True)
