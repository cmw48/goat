from django.db import models

# Create your models here.
# remember to makemigrations each time you change models
class Item(models.Model):
    text = models.TextField(default='')
