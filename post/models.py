from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class Post(models.Model):
    alphanumeric = RegexValidator(regex='^[a-zA-Z0-9 ]*$', message='Only alphanumeric characters are allowed.')
    author = models.CharField(max_length=200, validators=[alphanumeric])
    category = models.CharField(max_length=200, validators=[alphanumeric])
    title = models.CharField(max_length=200, validators=[alphanumeric])
    post = models.TextField()

    def __str__(self):
        return self.title
