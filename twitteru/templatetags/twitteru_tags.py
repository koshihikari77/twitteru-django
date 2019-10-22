from django import template

register = template.Library()


@register.filter
def is_in_likes(likes, post):
    result = likes.filter(post=post)
    return bool(result)*"like_on"


@register.filter
def is_in_follows(follows, user_pk):
    result = follows.filter(followed_user__id=user_pk)
    return bool(result)*"follow_on"
