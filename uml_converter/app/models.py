from django.db import models

# Create your models here.
class Entity(models.Model):
    actor = models.TextField()
    usecase = models.TextField()
    sentence = models.TextField()

  