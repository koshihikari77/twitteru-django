from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, null=True)
    self_introduction = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    website = models.URLField()
    tweet_open_flag = models.BooleanField()
    direct_message_flag = models.BooleanField()
    sensitive_flag = models.BooleanField()
    followed_num = models.IntegerField()


class Post(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    text = models.CharField(max_length=140)
    liked_num = models.IntegerField(default=0)
    replied_num = models.IntegerField(default=0)
    retweeted_num = models.IntegerField(default=0)
    reply_flag = models.BooleanField()

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
    replied_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='replied_post')
    replying_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='replying_post')


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    src = models.ImageField(upload_to='media')
    """
    thumbnail = ImageSpecField(source='src',
                               processors=[ResizeToFill(250, 250)],
                               format='JPEG',
                               options={'quality': 60})
                               """
