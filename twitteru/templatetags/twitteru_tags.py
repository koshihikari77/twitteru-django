from django import template
from ..models import Reply, Post
register = template.Library()


@register.filter
def is_in_likes(likes, post):
    result = likes.filter(post=post)
    return bool(result)*"like-on"


@register.filter
def is_in_follows(follows, user_pk):
    result = follows.filter(followed_user__id=user_pk)
    return bool(result)*"follow-on"


@register.filter
def replied_user(post):
    replied_post = Post.objects.filter(replied_post__replied_post=post)
    return replied_post[0].user
