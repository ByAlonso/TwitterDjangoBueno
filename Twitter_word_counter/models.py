from django.db import models

# Create your models here.

class WordList(models.Model):
    username = models.TextField(default=None)
    content = models.TextField()
