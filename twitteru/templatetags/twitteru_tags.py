from django import template

register = template.Library()


@register.filter
def is_in_likes(likes, post):
    result = likes.filter(post=post)
    return bool(result)*"on"
