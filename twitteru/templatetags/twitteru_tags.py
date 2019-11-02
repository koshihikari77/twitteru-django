from django import template
from ..models import Reply, Post
register = template.Library()


@register.filter
def is_in_likes(liking_post_ids, post_id):
    return (post_id in liking_post_ids)*"like-on"


@register.filter
def is_in_follows(following_user_ids, user_id):
    return (user_id in following_user_ids)*"follow-on"


@register.filter
def replied_user(post):
    replied_post = Post.objects.all().filter(
        replied_post_relation__replying_post=post).first()
    return replied_post.user
