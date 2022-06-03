# Generated by Django 4.0.4 on 2022-06-03 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=64, unique=True, verbose_name='название проекта')),
                ('repository_link', models.URLField(blank=True, verbose_name='ссылка на репозиторий')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='пользователи, работающие с проектом')),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('note_text', models.TextField(blank=True, verbose_name='текст заметки')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('execution_status', models.BooleanField(db_index=True, default=True, verbose_name='статус исполнения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.project', verbose_name='проект')),
            ],
        ),
    ]
