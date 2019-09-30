from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    text = models.CharField(max_length=140)
    replay_flag = models.BooleanField()


class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    self_introduction = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    website = models.URLField()
    tweet_open_flag = models.BooleanField()
    direct_message_flag = models.BooleanField()
    sensitive_flag = models.BooleanField()
