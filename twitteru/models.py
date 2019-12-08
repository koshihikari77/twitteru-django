from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model
# Create your models here.


class UserProfileManager(models.Manager):
    user_for_related_fields = True

    def all(self):
        qs = get_query_set().all()
        try:
            if self.instance:  # self.instanceはuser
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(),
                                related_name='profile', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, null=True)
    self_introduction = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    website = models.URLField()
    tweet_open_flag = models.BooleanField()
    direct_message_flag = models.BooleanField()
    sensitive_flag = models.BooleanField()
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')
    # user.profile.following ユーザーがフォローしているユーザーを返す
    # user.followed_by ユーザーをフォローしているユーザーを返す


class TweetManager(models.Manager):

    def like_toggle(self, user, tweet_obj):
        if user in tweet_obj.liked.all():
            is_liked = False
            tweet_obj.liked.remove(user)
        else:
            is_liked = True
            tweet_obj.liked.add(user)
        return is_liked


class Tweet(models.Model):
    parent = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=140)
    reply = models.BooleanField(default=False)
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='liked')

    objects = TweetManager()

    class Meta:
        ordering = ['timestamp']

    def get_parent(self):
        the_parent = self
        if self.parent:
            the_parent = self.parent
        return the_parent

    def get_children(self):
        parent = self.get_parent()
        qs = Tweet.objects.filter(parent=parent)
        qs_parent = Tweet.objects.filter(pk=parent.pk)
        return (qs | qs_parent)


class Image(models.Model):
    post = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    src = models.ImageField(upload_to='media')
    """
    thumbnail = ImageSpecField(source='src',
                               processors=[ResizeToFill(250, 250)],
                               format='JPEG',
                               options={'quality': 60})
                               """
