from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model
# Create your models here.


class UserSettings(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, null=True)
    self_introduction = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    website = models.URLField()
    tweet_open_flag = models.BooleanField()
    direct_message_flag = models.BooleanField()
    sensitive_flag = models.BooleanField()


class Post(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    text = models.CharField(max_length=140)
    liked_num = models.IntegerField(default=0)
    replayed_num = models.IntegerField(default=0)
    retweeted_num = models.IntegerField(default=0)
    replay_flag = models.BooleanField()

    class Meta:
        ordering = ['-posted_date']


class Follow(models.Model):
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_user')
    following_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following_user')


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Reply(models.Model):
    replayed_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='replayed_post')
    replaying_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='replaying_post')


class MediaFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    src = models.ImageField()
    thumbnail = ImageSpecField(source='src',
                               processors=[ResizeToFill(250, 250)],
                               format='JPEG',
                               options={'quality': 60})
