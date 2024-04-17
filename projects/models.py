from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.ImageField(upload_to='user/', null=True, blank=True)

class News(models.Model):
    title = models.CharField(max_length=45)
    text = models.TextField()
    rasm = models.ImageField(upload_to='news/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes')

# Create your models here.
