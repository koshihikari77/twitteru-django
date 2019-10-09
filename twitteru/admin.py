from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post
# Register your models here.

"""
class PostInline(admin.TabularInline):
    model = Post
    extra = 3


class CustomUserAdmin(UserAdmin):
    inlines = [PostInline]
"""


admin.site.register(Post)
