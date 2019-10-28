from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Profile, Image, Like, Follow, Reply
# Register your models here.

"""
class PostInline(admin.TabularInline):
    model = Post
    extra = 3


class CustomUserAdmin(UserAdmin):
    inlines = [PostInline]
"""


admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(Reply)

admin.site.register(Image)
