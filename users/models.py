from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    birthday = models.DateField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid4)

