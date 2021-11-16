from django.db import models
from django.conf import settings

# Create your models here.


class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.title


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.description
