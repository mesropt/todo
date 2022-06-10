from uuid import uuid4

from users.models import User
from django.db import models

# Самая важная часть модели - и единственная необходимая часть модели - это список полей базы данных, которые она определяет. Поля определяются атрибутами класса.
# СВЯЗИ ПИШЕМ В МОДЕЛЯХ
# Модель является единственным источником информации о ваших данных. Она содержит основные поля и поведение данных, которые вы храните. Как правило, каждая модель отображается в одну таблицу базы данных.
# Каждый атрибут модели представляет поле базы данных.


class Project(models.Model):  # ПРОЕКТ, ДЛЯ КОТОРОГО ЗАПИСАНЫ ЗАМЕТКИ
    uuid = models.UUIDField(default=uuid4)
    project_name = models.CharField("название проекта", max_length=128, unique=True)
    repository_link = models.URLField("ссылка на репозиторий", null=True, blank=True)
    users = models.ManyToManyField(User)  # Много пользователей - много проектов.

    def __str__(self):
        return self.project_name


class ToDo(models.Model):  # ЗАМЕТКА
    uuid = models.UUIDField(default=uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note_text = models.TextField("текст заметки", blank=True)
    date_created = models.DateTimeField("дата создания", auto_now_add=True)
    date_updated = models.DateTimeField("дата обновления", auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    execution_status = models.BooleanField("в процессе выполнения", default=True, db_index=True)
